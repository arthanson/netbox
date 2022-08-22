from utilities.permissions import get_permission_for_model


def get_prerequisite_model(queryset, user):
    model = queryset.model

    if not queryset.exists() and user.has_perms([get_permission_for_model(model, 'add'), ]):
        if hasattr(model, 'get_prerequisite_models'):
            prerequisites = model.get_prerequisite_models()
            if prerequisites:
                for prereq in prerequisites:
                    if not prereq.objects.exists() and user.has_perms([get_permission_for_model(prereq, 'add'), ]):
                        return prereq

    return None
