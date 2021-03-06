#!/usr/bin/env python

#
# Generated Wed Oct 10 14:18:14 2018 by generateDS.py version 2.29.24.
# Python 3.6.5 (default, May 11 2018, 13:30:17)  [GCC 7.3.0]
#
# Command line options:
#   ('-o', 'classes/evtAltCadastral.py')
#   ('-s', 'classes/evtAltCadastralSub.py')
#   ('--super', 'evtAltCadastral')
#
# Command line arguments:
#   /home/joao/Documents/teste_xsd/xsd/evtAltCadastral.xsd
#
# Command line:
#   /home/joao/Documents/teste_xsd/dkuhlman-generateds-60c208fd6e8d/generateDS.py -o "classes/evtAltCadastral.py" -s "classes/evtAltCadastralSub.py" --super="evtAltCadastral" /home/joao/Documents/teste_xsd/xsd/evtAltCadastral.xsd
#
# Current working directory (os.getcwd()):
#   teste_xsd
#

import sys
from lxml import etree as etree_

import evtAltCadastral as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = ''

#
# Data representation classes
#


class eSocialSub(supermod.eSocial):
    def __init__(self, evtAltCadastral=None, Signature=None):
        super(eSocialSub, self).__init__(evtAltCadastral, Signature, )
supermod.eSocial.subclass = eSocialSub
# end class eSocialSub


class TIdeEveTrabSub(supermod.TIdeEveTrab):
    def __init__(self, indRetif=None, nrRecibo=None, tpAmb=None, procEmi=None, verProc=None):
        super(TIdeEveTrabSub, self).__init__(indRetif, nrRecibo, tpAmb, procEmi, verProc, )
supermod.TIdeEveTrab.subclass = TIdeEveTrabSub
# end class TIdeEveTrabSub


class TEmpregadorSub(supermod.TEmpregador):
    def __init__(self, tpInsc=None, nrInsc=None):
        super(TEmpregadorSub, self).__init__(tpInsc, nrInsc, )
supermod.TEmpregador.subclass = TEmpregadorSub
# end class TEmpregadorSub


class TCtpsSub(supermod.TCtps):
    def __init__(self, nrCtps=None, serieCtps=None, ufCtps=None):
        super(TCtpsSub, self).__init__(nrCtps, serieCtps, ufCtps, )
supermod.TCtps.subclass = TCtpsSub
# end class TCtpsSub


class TRicSub(supermod.TRic):
    def __init__(self, nrRic=None, orgaoEmissor=None, dtExped=None):
        super(TRicSub, self).__init__(nrRic, orgaoEmissor, dtExped, )
supermod.TRic.subclass = TRicSub
# end class TRicSub


class TRgSub(supermod.TRg):
    def __init__(self, nrRg=None, orgaoEmissor=None, dtExped=None):
        super(TRgSub, self).__init__(nrRg, orgaoEmissor, dtExped, )
supermod.TRg.subclass = TRgSub
# end class TRgSub


class TRneSub(supermod.TRne):
    def __init__(self, nrRne=None, orgaoEmissor=None, dtExped=None):
        super(TRneSub, self).__init__(nrRne, orgaoEmissor, dtExped, )
supermod.TRne.subclass = TRneSub
# end class TRneSub


class TOcSub(supermod.TOc):
    def __init__(self, nrOc=None, orgaoEmissor=None, dtExped=None, dtValid=None):
        super(TOcSub, self).__init__(nrOc, orgaoEmissor, dtExped, dtValid, )
supermod.TOc.subclass = TOcSub
# end class TOcSub


class TCnhSub(supermod.TCnh):
    def __init__(self, nrRegCnh=None, dtExped=None, ufCnh=None, dtValid=None, dtPriHab=None, categoriaCnh=None):
        super(TCnhSub, self).__init__(nrRegCnh, dtExped, ufCnh, dtValid, dtPriHab, categoriaCnh, )
supermod.TCnh.subclass = TCnhSub
# end class TCnhSub


class TEnderecoBrasilSub(supermod.TEnderecoBrasil):
    def __init__(self, tpLograd=None, dscLograd=None, nrLograd=None, complemento=None, bairro=None, cep=None, codMunic=None, uf=None):
        super(TEnderecoBrasilSub, self).__init__(tpLograd, dscLograd, nrLograd, complemento, bairro, cep, codMunic, uf, )
supermod.TEnderecoBrasil.subclass = TEnderecoBrasilSub
# end class TEnderecoBrasilSub


class TEnderecoExteriorSub(supermod.TEnderecoExterior):
    def __init__(self, paisResid=None, dscLograd=None, nrLograd=None, complemento=None, bairro=None, nmCid=None, codPostal=None):
        super(TEnderecoExteriorSub, self).__init__(paisResid, dscLograd, nrLograd, complemento, bairro, nmCid, codPostal, )
supermod.TEnderecoExterior.subclass = TEnderecoExteriorSub
# end class TEnderecoExteriorSub


class TTrabEstrangSub(supermod.TTrabEstrang):
    def __init__(self, dtChegada=None, classTrabEstrang=None, casadoBr=None, filhosBr=None):
        super(TTrabEstrangSub, self).__init__(dtChegada, classTrabEstrang, casadoBr, filhosBr, )
supermod.TTrabEstrang.subclass = TTrabEstrangSub
# end class TTrabEstrangSub


class TDependenteSub(supermod.TDependente):
    def __init__(self, tpDep=None, nmDep=None, dtNascto=None, cpfDep=None, depIRRF=None, depSF=None, incTrab=None):
        super(TDependenteSub, self).__init__(tpDep, nmDep, dtNascto, cpfDep, depIRRF, depSF, incTrab, )
supermod.TDependente.subclass = TDependenteSub
# end class TDependenteSub


class TContatoSub(supermod.TContato):
    def __init__(self, fonePrinc=None, foneAlternat=None, emailPrinc=None, emailAlternat=None):
        super(TContatoSub, self).__init__(fonePrinc, foneAlternat, emailPrinc, emailAlternat, )
supermod.TContato.subclass = TContatoSub
# end class TContatoSub


class SignatureTypeSub(supermod.SignatureType):
    def __init__(self, Id=None, SignedInfo=None, SignatureValue=None, KeyInfo=None, Object=None):
        super(SignatureTypeSub, self).__init__(Id, SignedInfo, SignatureValue, KeyInfo, Object, )
supermod.SignatureType.subclass = SignatureTypeSub
# end class SignatureTypeSub


class SignatureValueTypeSub(supermod.SignatureValueType):
    def __init__(self, Id=None, valueOf_=None):
        super(SignatureValueTypeSub, self).__init__(Id, valueOf_, )
supermod.SignatureValueType.subclass = SignatureValueTypeSub
# end class SignatureValueTypeSub


class SignedInfoTypeSub(supermod.SignedInfoType):
    def __init__(self, Id=None, CanonicalizationMethod=None, SignatureMethod=None, Reference=None):
        super(SignedInfoTypeSub, self).__init__(Id, CanonicalizationMethod, SignatureMethod, Reference, )
supermod.SignedInfoType.subclass = SignedInfoTypeSub
# end class SignedInfoTypeSub


class CanonicalizationMethodTypeSub(supermod.CanonicalizationMethodType):
    def __init__(self, Algorithm=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(CanonicalizationMethodTypeSub, self).__init__(Algorithm, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.CanonicalizationMethodType.subclass = CanonicalizationMethodTypeSub
# end class CanonicalizationMethodTypeSub


class SignatureMethodTypeSub(supermod.SignatureMethodType):
    def __init__(self, Algorithm=None, HMACOutputLength=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(SignatureMethodTypeSub, self).__init__(Algorithm, HMACOutputLength, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.SignatureMethodType.subclass = SignatureMethodTypeSub
# end class SignatureMethodTypeSub


class ReferenceTypeSub(supermod.ReferenceType):
    def __init__(self, Id=None, URI=None, Type=None, Transforms=None, DigestMethod=None, DigestValue=None):
        super(ReferenceTypeSub, self).__init__(Id, URI, Type, Transforms, DigestMethod, DigestValue, )
supermod.ReferenceType.subclass = ReferenceTypeSub
# end class ReferenceTypeSub


class TransformsTypeSub(supermod.TransformsType):
    def __init__(self, Transform=None):
        super(TransformsTypeSub, self).__init__(Transform, )
supermod.TransformsType.subclass = TransformsTypeSub
# end class TransformsTypeSub


class TransformTypeSub(supermod.TransformType):
    def __init__(self, Algorithm=None, anytypeobjs_=None, XPath=None, valueOf_=None, mixedclass_=None, content_=None):
        super(TransformTypeSub, self).__init__(Algorithm, anytypeobjs_, XPath, valueOf_, mixedclass_, content_, )
supermod.TransformType.subclass = TransformTypeSub
# end class TransformTypeSub


class DigestMethodTypeSub(supermod.DigestMethodType):
    def __init__(self, Algorithm=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(DigestMethodTypeSub, self).__init__(Algorithm, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.DigestMethodType.subclass = DigestMethodTypeSub
# end class DigestMethodTypeSub


class KeyInfoTypeSub(supermod.KeyInfoType):
    def __init__(self, Id=None, KeyName=None, KeyValue=None, RetrievalMethod=None, X509Data=None, PGPData=None, SPKIData=None, MgmtData=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(KeyInfoTypeSub, self).__init__(Id, KeyName, KeyValue, RetrievalMethod, X509Data, PGPData, SPKIData, MgmtData, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.KeyInfoType.subclass = KeyInfoTypeSub
# end class KeyInfoTypeSub


class KeyValueTypeSub(supermod.KeyValueType):
    def __init__(self, DSAKeyValue=None, RSAKeyValue=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(KeyValueTypeSub, self).__init__(DSAKeyValue, RSAKeyValue, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.KeyValueType.subclass = KeyValueTypeSub
# end class KeyValueTypeSub


class RetrievalMethodTypeSub(supermod.RetrievalMethodType):
    def __init__(self, URI=None, Type=None, Transforms=None):
        super(RetrievalMethodTypeSub, self).__init__(URI, Type, Transforms, )
supermod.RetrievalMethodType.subclass = RetrievalMethodTypeSub
# end class RetrievalMethodTypeSub


class X509DataTypeSub(supermod.X509DataType):
    def __init__(self, X509IssuerSerial=None, X509SKI=None, X509SubjectName=None, X509Certificate=None, X509CRL=None, anytypeobjs_=None):
        super(X509DataTypeSub, self).__init__(X509IssuerSerial, X509SKI, X509SubjectName, X509Certificate, X509CRL, anytypeobjs_, )
supermod.X509DataType.subclass = X509DataTypeSub
# end class X509DataTypeSub


class X509IssuerSerialTypeSub(supermod.X509IssuerSerialType):
    def __init__(self, X509IssuerName=None, X509SerialNumber=None):
        super(X509IssuerSerialTypeSub, self).__init__(X509IssuerName, X509SerialNumber, )
supermod.X509IssuerSerialType.subclass = X509IssuerSerialTypeSub
# end class X509IssuerSerialTypeSub


class PGPDataTypeSub(supermod.PGPDataType):
    def __init__(self, PGPKeyID=None, PGPKeyPacket=None, anytypeobjs_=None):
        super(PGPDataTypeSub, self).__init__(PGPKeyID, PGPKeyPacket, anytypeobjs_, )
supermod.PGPDataType.subclass = PGPDataTypeSub
# end class PGPDataTypeSub


class SPKIDataTypeSub(supermod.SPKIDataType):
    def __init__(self, SPKISexp=None, anytypeobjs_=None):
        super(SPKIDataTypeSub, self).__init__(SPKISexp, anytypeobjs_, )
supermod.SPKIDataType.subclass = SPKIDataTypeSub
# end class SPKIDataTypeSub


class ObjectTypeSub(supermod.ObjectType):
    def __init__(self, Id=None, MimeType=None, Encoding=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(ObjectTypeSub, self).__init__(Id, MimeType, Encoding, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.ObjectType.subclass = ObjectTypeSub
# end class ObjectTypeSub


class ManifestTypeSub(supermod.ManifestType):
    def __init__(self, Id=None, Reference=None):
        super(ManifestTypeSub, self).__init__(Id, Reference, )
supermod.ManifestType.subclass = ManifestTypeSub
# end class ManifestTypeSub


class SignaturePropertiesTypeSub(supermod.SignaturePropertiesType):
    def __init__(self, Id=None, SignatureProperty=None):
        super(SignaturePropertiesTypeSub, self).__init__(Id, SignatureProperty, )
supermod.SignaturePropertiesType.subclass = SignaturePropertiesTypeSub
# end class SignaturePropertiesTypeSub


class SignaturePropertyTypeSub(supermod.SignaturePropertyType):
    def __init__(self, Target=None, Id=None, anytypeobjs_=None, valueOf_=None, mixedclass_=None, content_=None):
        super(SignaturePropertyTypeSub, self).__init__(Target, Id, anytypeobjs_, valueOf_, mixedclass_, content_, )
supermod.SignaturePropertyType.subclass = SignaturePropertyTypeSub
# end class SignaturePropertyTypeSub


class DSAKeyValueTypeSub(supermod.DSAKeyValueType):
    def __init__(self, P=None, Q=None, G=None, Y=None, J=None, Seed=None, PgenCounter=None):
        super(DSAKeyValueTypeSub, self).__init__(P, Q, G, Y, J, Seed, PgenCounter, )
supermod.DSAKeyValueType.subclass = DSAKeyValueTypeSub
# end class DSAKeyValueTypeSub


class RSAKeyValueTypeSub(supermod.RSAKeyValueType):
    def __init__(self, Modulus=None, Exponent=None):
        super(RSAKeyValueTypeSub, self).__init__(Modulus, Exponent, )
supermod.RSAKeyValueType.subclass = RSAKeyValueTypeSub
# end class RSAKeyValueTypeSub


class evtAltCadastralTypeSub(supermod.evtAltCadastralType):
    def __init__(self, Id=None, ideEvento=None, ideEmpregador=None, ideTrabalhador=None, alteracao=None):
        super(evtAltCadastralTypeSub, self).__init__(Id, ideEvento, ideEmpregador, ideTrabalhador, alteracao, )
supermod.evtAltCadastralType.subclass = evtAltCadastralTypeSub
# end class evtAltCadastralTypeSub


class ideTrabalhadorTypeSub(supermod.ideTrabalhadorType):
    def __init__(self, cpfTrab=None):
        super(ideTrabalhadorTypeSub, self).__init__(cpfTrab, )
supermod.ideTrabalhadorType.subclass = ideTrabalhadorTypeSub
# end class ideTrabalhadorTypeSub


class alteracaoTypeSub(supermod.alteracaoType):
    def __init__(self, dtAlteracao=None, dadosTrabalhador=None):
        super(alteracaoTypeSub, self).__init__(dtAlteracao, dadosTrabalhador, )
supermod.alteracaoType.subclass = alteracaoTypeSub
# end class alteracaoTypeSub


class dadosTrabalhadorTypeSub(supermod.dadosTrabalhadorType):
    def __init__(self, nisTrab=None, nmTrab=None, sexo=None, racaCor=None, estCiv=None, grauInstr=None, nmSoc=None, nascimento=None, documentos=None, endereco=None, trabEstrangeiro=None, infoDeficiencia=None, dependente=None, aposentadoria=None, contato=None):
        super(dadosTrabalhadorTypeSub, self).__init__(nisTrab, nmTrab, sexo, racaCor, estCiv, grauInstr, nmSoc, nascimento, documentos, endereco, trabEstrangeiro, infoDeficiencia, dependente, aposentadoria, contato, )
supermod.dadosTrabalhadorType.subclass = dadosTrabalhadorTypeSub
# end class dadosTrabalhadorTypeSub


class nascimentoTypeSub(supermod.nascimentoType):
    def __init__(self, dtNascto=None, codMunic=None, uf=None, paisNascto=None, paisNac=None, nmMae=None, nmPai=None):
        super(nascimentoTypeSub, self).__init__(dtNascto, codMunic, uf, paisNascto, paisNac, nmMae, nmPai, )
supermod.nascimentoType.subclass = nascimentoTypeSub
# end class nascimentoTypeSub


class documentosTypeSub(supermod.documentosType):
    def __init__(self, CTPS=None, RIC=None, RG=None, RNE=None, OC=None, CNH=None):
        super(documentosTypeSub, self).__init__(CTPS, RIC, RG, RNE, OC, CNH, )
supermod.documentosType.subclass = documentosTypeSub
# end class documentosTypeSub


class enderecoTypeSub(supermod.enderecoType):
    def __init__(self, brasil=None, exterior=None):
        super(enderecoTypeSub, self).__init__(brasil, exterior, )
supermod.enderecoType.subclass = enderecoTypeSub
# end class enderecoTypeSub


class infoDeficienciaTypeSub(supermod.infoDeficienciaType):
    def __init__(self, defFisica=None, defVisual=None, defAuditiva=None, defMental=None, defIntelectual=None, reabReadap=None, infoCota=None, observacao=None):
        super(infoDeficienciaTypeSub, self).__init__(defFisica, defVisual, defAuditiva, defMental, defIntelectual, reabReadap, infoCota, observacao, )
supermod.infoDeficienciaType.subclass = infoDeficienciaTypeSub
# end class infoDeficienciaTypeSub


class aposentadoriaTypeSub(supermod.aposentadoriaType):
    def __init__(self, trabAposent=None):
        super(aposentadoriaTypeSub, self).__init__(trabAposent, )
supermod.aposentadoriaType.subclass = aposentadoriaTypeSub
# end class aposentadoriaTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'eSocial'
        rootClass = supermod.eSocial
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'eSocial'
        rootClass = supermod.eSocial
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'eSocial'
        rootClass = supermod.eSocial
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'eSocial'
        rootClass = supermod.eSocial
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from evtAltCadastral import *\n\n')
        sys.stdout.write('import evtAltCadastral as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
