import evtInfoEmpregador
import evtInfoEmpregadorSub


class Test:
    contato = evtInfoEmpregadorSub.contatoTypeSub(
        nmCtt='Fulano', cpfCtt='00000000000', foneFixo='61999999999', email='abcd@gmail.br')

    info_complementares = evtInfoEmpregadorSub.infoComplementaresTypeSub(
        situacaoPJ=evtInfoEmpregadorSub.situacaoPJTypeSub(indSitPJ='0'))

    cadastro = evtInfoEmpregadorSub.TInfoEmpregadorSub(nmRazao='Orgao', classTrib='85',
                                                       natJurid='1010', indCoop='0', indConstr='0', indDesFolha='0', indOptRegEletron='1', indEntEd='N', indEtt='N',
                                                       contato=contato, infoOP=evtInfoEmpregadorSub.infoOPTypeSub(nrSiafi='000001'), infoComplementares=info_complementares)

    periodo = evtInfoEmpregadorSub.TIdePeriodoSub(iniValid='2018-10')

    info_empregador = evtInfoEmpregadorSub.inclusaoTypeSub(
        idePeriodo=periodo, infoCadastro=cadastro)
    
    inclusao = evtInfoEmpregadorSub.infoEmpregadorTypeSub(inclusao=info_empregador)

    id_evento = evtInfoEmpregadorSub.TIdeCadastroSub(
        tpAmb='2', procEmi='1', verProc='1.0.0')

    id_empregador = evtInfoEmpregadorSub.TEmpregadorSub(
        tpInsc='1', nrInsc='00501000000120')

    evt_info_empregador = evtInfoEmpregadorSub.evtInfoEmpregadorTypeSub(
        Id='ID1000016400000202018100000545700000', ideEvento=id_evento, ideEmpregador=id_empregador, infoEmpregador=inclusao)
        
    evtInfoEmpregadorSub.eSocialSub(
        evt_info_empregador).export(open('xml_gerado.xml', 'w'), 0, namespacedef_='xmlns="http://www.esocial.gov.br/schema/evt/evtInfoEmpregador/v02_04_02" xmlns:ns2="http://www.w3.org/2000/09/xmldsig#"')

    my_file = open('xml_gerado.xml', "r")
    lines_of_file = my_file.readlines()
    lines_of_file.insert(0, '<?xml version="1.0" encoding="UTF-8"?>\n')
    my_file = open('xml_gerado.xml', "w")
    my_file.writelines(lines_of_file)
