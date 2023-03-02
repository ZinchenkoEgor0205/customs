class Person:
    def __init__(self):
        super().__init__()
        pass

    def name_surname_last_name_to_rp(self):
        a_letters_set = 'кнгзфвпрлджчмтб'
        freeze_letters_set = 'о'
        output = []
        for obj in [self.surname, self.name, self.last_name]:
            if obj[-1] in a_letters_set:
                obj += 'а'
            elif obj[-1] in freeze_letters_set:
                pass
            else:
                obj += 'я'
            output.append(obj)
        return ' '.join(output)

    def name_last_name_to_initials(self):
        return f'{self.surname} {self.name[0]}.{self.last_name[0]}.'


class Criminal(Person):

    def citizenship_to_rp(self):
        hard_letters_set = 'кнгзфвпрлджчмтб'
        output = self.citizenship.split()
        if output[0][-1] in hard_letters_set:
            output[0] = output[0][:-1] + 'ы'
        else:
            output[0] = output[0][:-1] + 'и'

        return ' '.join(output)

    def place_of_living_to_rp(self):
        hard_letters_set = 'кнгзфвпрлджчмтб'
        output = self.place_of_living.split()
        if output[0][-1] in hard_letters_set:
            output[0] = output[0][:-1] + 'ы'
        else:
            output[0] = output[0][:-1] + 'и'

        return ' '.join(output)


class Inspector(Person):
    pass


class MixedData:
    pass
