import clips

if __name__ == "__main__":
    env = clips.Environment()

    # Ordered facts can only be asserted as strings
    fact = env.assert_string('(ordered-fact 1 2 3)')

    # Ordered facts data can be accessed as list elements
    assert fact[0] == 1
    assert list(fact) == [1, 2, 3]

    for fact in env.facts():
        print(fact)

    # template_string = """
    # (deftemplate person
    # (slot name (type STRING))
    # (slot surname (type STRING))
    # (slot birthdate (type SYMBOL)))
    # """
    # env = clips.Environment()
    # env.build(template_string)
    # template = env.find_template('person')
    # fact = template.assert_fact(name='John',
    #                             surname='Doe',
    #                             birthdate=clips.Symbol('01/01/1970'))
    # assert dict(fact) == {'name': 'John',
    #                       'surname': 'Doe',
    #                       'birthdate': clips.Symbol('01/01/1970')}
    # fact.modify_slots(name='Leeroy',
    #                   surname='Jenkins',
    #                   birthdate=clips.Symbol('11/05/2005'))
    # for fact in env.facts():
    #     print(fact)