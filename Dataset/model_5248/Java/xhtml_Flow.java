





import java.util.List;
import java.util.ArrayList;

public class xhtml_Flow  {

    private String group;
    private String mixed;





    private List<xhtml_SubType> xhtml_subtypes;




    private List<xhtml_StrikeType> xhtml_striketypes;




    private List<xhtml_CodeType> xhtml_codetypes;




    private List<xhtml_ObjectType> xhtml_objecttypes;




    private List<xhtml_ImgType> xhtml_imgtypes;




    private List<xhtml_QType> xhtml_qtypes;




    private List<xhtml_H2Type> xhtml_h2types;




    private List<xhtml_TableType> xhtml_tabletypes;




    private List<xhtml_HrType> xhtml_hrtypes;




    private List<xhtml_H3Type> xhtml_h3types;




    private List<xhtml_IType> xhtml_itypes;




    private List<xhtml_DfnType> xhtml_dfntypes;




    private List<xhtml_H1Type> xhtml_h1types;




    private List<xhtml_H4Type> xhtml_h4types;




    private List<xhtml_PType> xhtml_ptypes;




    private List<xhtml_BType> xhtml_btypes;




    private List<xhtml_TtType> xhtml_tttypes;




    private List<xhtml_InsType> xhtml_instypes;




    private List<xhtml_CiteType> xhtml_citetypes;




    private List<xhtml_VarType> xhtml_vartypes;




    private List<xhtml_KbdType> xhtml_kbdtypes;




    private List<xhtml_EmType> xhtml_emtypes;




    private List<xhtml_SampType> xhtml_samptypes;




    private List<xhtml_AcronymType> xhtml_acronymtypes;




    private List<xhtml_DivType> xhtml_divtypes;




    private List<xhtml_AddressType> xhtml_addresstypes;




    private List<xhtml_SmallType> xhtml_smalltypes;




    private List<xhtml_DelType> xhtml_deltypes;




    private List<xhtml_StrongType> xhtml_strongtypes;




    private List<xhtml_H6Type> xhtml_h6types;




    private List<xhtml_BrType> xhtml_brtypes;




    private List<xhtml_BlockquoteType> xhtml_blockquotetypes;




    private List<xhtml_AbbrType> xhtml_abbrtypes;




    private List<xhtml_BigType> xhtml_bigtypes;




    private List<xhtml_SupType> xhtml_suptypes;




    private List<xhtml_SpanType> xhtml_spantypes;




    private List<xhtml_H5Type> xhtml_h5types;




    private List<xhtml_UType> xhtml_utypes;


    public xhtml_Flow(
        String group,        String mixed    ) {
        this.group = group;
        this.mixed = mixed;
        this.xhtml_subtypes = new ArrayList<>();
        this.xhtml_striketypes = new ArrayList<>();
        this.xhtml_codetypes = new ArrayList<>();
        this.xhtml_objecttypes = new ArrayList<>();
        this.xhtml_imgtypes = new ArrayList<>();
        this.xhtml_qtypes = new ArrayList<>();
        this.xhtml_h2types = new ArrayList<>();
        this.xhtml_tabletypes = new ArrayList<>();
        this.xhtml_hrtypes = new ArrayList<>();
        this.xhtml_h3types = new ArrayList<>();
        this.xhtml_itypes = new ArrayList<>();
        this.xhtml_dfntypes = new ArrayList<>();
        this.xhtml_h1types = new ArrayList<>();
        this.xhtml_h4types = new ArrayList<>();
        this.xhtml_ptypes = new ArrayList<>();
        this.xhtml_btypes = new ArrayList<>();
        this.xhtml_tttypes = new ArrayList<>();
        this.xhtml_instypes = new ArrayList<>();
        this.xhtml_citetypes = new ArrayList<>();
        this.xhtml_vartypes = new ArrayList<>();
        this.xhtml_kbdtypes = new ArrayList<>();
        this.xhtml_emtypes = new ArrayList<>();
        this.xhtml_samptypes = new ArrayList<>();
        this.xhtml_acronymtypes = new ArrayList<>();
        this.xhtml_divtypes = new ArrayList<>();
        this.xhtml_addresstypes = new ArrayList<>();
        this.xhtml_smalltypes = new ArrayList<>();
        this.xhtml_deltypes = new ArrayList<>();
        this.xhtml_strongtypes = new ArrayList<>();
        this.xhtml_h6types = new ArrayList<>();
        this.xhtml_brtypes = new ArrayList<>();
        this.xhtml_blockquotetypes = new ArrayList<>();
        this.xhtml_abbrtypes = new ArrayList<>();
        this.xhtml_bigtypes = new ArrayList<>();
        this.xhtml_suptypes = new ArrayList<>();
        this.xhtml_spantypes = new ArrayList<>();
        this.xhtml_h5types = new ArrayList<>();
        this.xhtml_utypes = new ArrayList<>();
    }

    public xhtml_Flow(
        String group,        String mixed        ArrayList<xhtml_SubType> xhtml_subtypes,        ArrayList<xhtml_StrikeType> xhtml_striketypes,        ArrayList<xhtml_CodeType> xhtml_codetypes,        ArrayList<xhtml_ObjectType> xhtml_objecttypes,        ArrayList<xhtml_ImgType> xhtml_imgtypes,        ArrayList<xhtml_QType> xhtml_qtypes,        ArrayList<xhtml_H2Type> xhtml_h2types,        ArrayList<xhtml_TableType> xhtml_tabletypes,        ArrayList<xhtml_HrType> xhtml_hrtypes,        ArrayList<xhtml_H3Type> xhtml_h3types,        ArrayList<xhtml_IType> xhtml_itypes,        ArrayList<xhtml_DfnType> xhtml_dfntypes,        ArrayList<xhtml_H1Type> xhtml_h1types,        ArrayList<xhtml_H4Type> xhtml_h4types,        ArrayList<xhtml_PType> xhtml_ptypes,        ArrayList<xhtml_BType> xhtml_btypes,        ArrayList<xhtml_TtType> xhtml_tttypes,        ArrayList<xhtml_InsType> xhtml_instypes,        ArrayList<xhtml_CiteType> xhtml_citetypes,        ArrayList<xhtml_VarType> xhtml_vartypes,        ArrayList<xhtml_KbdType> xhtml_kbdtypes,        ArrayList<xhtml_EmType> xhtml_emtypes,        ArrayList<xhtml_SampType> xhtml_samptypes,        ArrayList<xhtml_AcronymType> xhtml_acronymtypes,        ArrayList<xhtml_DivType> xhtml_divtypes,        ArrayList<xhtml_AddressType> xhtml_addresstypes,        ArrayList<xhtml_SmallType> xhtml_smalltypes,        ArrayList<xhtml_DelType> xhtml_deltypes,        ArrayList<xhtml_StrongType> xhtml_strongtypes,        ArrayList<xhtml_H6Type> xhtml_h6types,        ArrayList<xhtml_BrType> xhtml_brtypes,        ArrayList<xhtml_BlockquoteType> xhtml_blockquotetypes,        ArrayList<xhtml_AbbrType> xhtml_abbrtypes,        ArrayList<xhtml_BigType> xhtml_bigtypes,        ArrayList<xhtml_SupType> xhtml_suptypes,        ArrayList<xhtml_SpanType> xhtml_spantypes,        ArrayList<xhtml_H5Type> xhtml_h5types,        ArrayList<xhtml_UType> xhtml_utypes    ) {
        this.group = group;
        this.mixed = mixed;
        this.xhtml_subtypes = xhtml_subtypes;
        this.xhtml_striketypes = xhtml_striketypes;
        this.xhtml_codetypes = xhtml_codetypes;
        this.xhtml_objecttypes = xhtml_objecttypes;
        this.xhtml_imgtypes = xhtml_imgtypes;
        this.xhtml_qtypes = xhtml_qtypes;
        this.xhtml_h2types = xhtml_h2types;
        this.xhtml_tabletypes = xhtml_tabletypes;
        this.xhtml_hrtypes = xhtml_hrtypes;
        this.xhtml_h3types = xhtml_h3types;
        this.xhtml_itypes = xhtml_itypes;
        this.xhtml_dfntypes = xhtml_dfntypes;
        this.xhtml_h1types = xhtml_h1types;
        this.xhtml_h4types = xhtml_h4types;
        this.xhtml_ptypes = xhtml_ptypes;
        this.xhtml_btypes = xhtml_btypes;
        this.xhtml_tttypes = xhtml_tttypes;
        this.xhtml_instypes = xhtml_instypes;
        this.xhtml_citetypes = xhtml_citetypes;
        this.xhtml_vartypes = xhtml_vartypes;
        this.xhtml_kbdtypes = xhtml_kbdtypes;
        this.xhtml_emtypes = xhtml_emtypes;
        this.xhtml_samptypes = xhtml_samptypes;
        this.xhtml_acronymtypes = xhtml_acronymtypes;
        this.xhtml_divtypes = xhtml_divtypes;
        this.xhtml_addresstypes = xhtml_addresstypes;
        this.xhtml_smalltypes = xhtml_smalltypes;
        this.xhtml_deltypes = xhtml_deltypes;
        this.xhtml_strongtypes = xhtml_strongtypes;
        this.xhtml_h6types = xhtml_h6types;
        this.xhtml_brtypes = xhtml_brtypes;
        this.xhtml_blockquotetypes = xhtml_blockquotetypes;
        this.xhtml_abbrtypes = xhtml_abbrtypes;
        this.xhtml_bigtypes = xhtml_bigtypes;
        this.xhtml_suptypes = xhtml_suptypes;
        this.xhtml_spantypes = xhtml_spantypes;
        this.xhtml_h5types = xhtml_h5types;
        this.xhtml_utypes = xhtml_utypes;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<xhtml_SubType> getXhtml_subtypes() {
        return xhtml_subtypes;
    }

    public void addXhtml_subtype(Xhtml_subtype xhtml_subtype) {
        this.xhtml_subtypes.add(xhtml_subtype);
    }
    public List<xhtml_StrikeType> getXhtml_striketypes() {
        return xhtml_striketypes;
    }

    public void addXhtml_striketype(Xhtml_striketype xhtml_striketype) {
        this.xhtml_striketypes.add(xhtml_striketype);
    }
    public List<xhtml_CodeType> getXhtml_codetypes() {
        return xhtml_codetypes;
    }

    public void addXhtml_codetype(Xhtml_codetype xhtml_codetype) {
        this.xhtml_codetypes.add(xhtml_codetype);
    }
    public List<xhtml_ObjectType> getXhtml_objecttypes() {
        return xhtml_objecttypes;
    }

    public void addXhtml_objecttype(Xhtml_objecttype xhtml_objecttype) {
        this.xhtml_objecttypes.add(xhtml_objecttype);
    }
    public List<xhtml_ImgType> getXhtml_imgtypes() {
        return xhtml_imgtypes;
    }

    public void addXhtml_imgtype(Xhtml_imgtype xhtml_imgtype) {
        this.xhtml_imgtypes.add(xhtml_imgtype);
    }
    public List<xhtml_QType> getXhtml_qtypes() {
        return xhtml_qtypes;
    }

    public void addXhtml_qtype(Xhtml_qtype xhtml_qtype) {
        this.xhtml_qtypes.add(xhtml_qtype);
    }
    public List<xhtml_H2Type> getXhtml_h2types() {
        return xhtml_h2types;
    }

    public void addXhtml_h2type(Xhtml_h2type xhtml_h2type) {
        this.xhtml_h2types.add(xhtml_h2type);
    }
    public List<xhtml_TableType> getXhtml_tabletypes() {
        return xhtml_tabletypes;
    }

    public void addXhtml_tabletype(Xhtml_tabletype xhtml_tabletype) {
        this.xhtml_tabletypes.add(xhtml_tabletype);
    }
    public List<xhtml_HrType> getXhtml_hrtypes() {
        return xhtml_hrtypes;
    }

    public void addXhtml_hrtype(Xhtml_hrtype xhtml_hrtype) {
        this.xhtml_hrtypes.add(xhtml_hrtype);
    }
    public List<xhtml_H3Type> getXhtml_h3types() {
        return xhtml_h3types;
    }

    public void addXhtml_h3type(Xhtml_h3type xhtml_h3type) {
        this.xhtml_h3types.add(xhtml_h3type);
    }
    public List<xhtml_IType> getXhtml_itypes() {
        return xhtml_itypes;
    }

    public void addXhtml_itype(Xhtml_itype xhtml_itype) {
        this.xhtml_itypes.add(xhtml_itype);
    }
    public List<xhtml_DfnType> getXhtml_dfntypes() {
        return xhtml_dfntypes;
    }

    public void addXhtml_dfntype(Xhtml_dfntype xhtml_dfntype) {
        this.xhtml_dfntypes.add(xhtml_dfntype);
    }
    public List<xhtml_H1Type> getXhtml_h1types() {
        return xhtml_h1types;
    }

    public void addXhtml_h1type(Xhtml_h1type xhtml_h1type) {
        this.xhtml_h1types.add(xhtml_h1type);
    }
    public List<xhtml_H4Type> getXhtml_h4types() {
        return xhtml_h4types;
    }

    public void addXhtml_h4type(Xhtml_h4type xhtml_h4type) {
        this.xhtml_h4types.add(xhtml_h4type);
    }
    public List<xhtml_PType> getXhtml_ptypes() {
        return xhtml_ptypes;
    }

    public void addXhtml_ptype(Xhtml_ptype xhtml_ptype) {
        this.xhtml_ptypes.add(xhtml_ptype);
    }
    public List<xhtml_BType> getXhtml_btypes() {
        return xhtml_btypes;
    }

    public void addXhtml_btype(Xhtml_btype xhtml_btype) {
        this.xhtml_btypes.add(xhtml_btype);
    }
    public List<xhtml_TtType> getXhtml_tttypes() {
        return xhtml_tttypes;
    }

    public void addXhtml_tttype(Xhtml_tttype xhtml_tttype) {
        this.xhtml_tttypes.add(xhtml_tttype);
    }
    public List<xhtml_InsType> getXhtml_instypes() {
        return xhtml_instypes;
    }

    public void addXhtml_instype(Xhtml_instype xhtml_instype) {
        this.xhtml_instypes.add(xhtml_instype);
    }
    public List<xhtml_CiteType> getXhtml_citetypes() {
        return xhtml_citetypes;
    }

    public void addXhtml_citetype(Xhtml_citetype xhtml_citetype) {
        this.xhtml_citetypes.add(xhtml_citetype);
    }
    public List<xhtml_VarType> getXhtml_vartypes() {
        return xhtml_vartypes;
    }

    public void addXhtml_vartype(Xhtml_vartype xhtml_vartype) {
        this.xhtml_vartypes.add(xhtml_vartype);
    }
    public List<xhtml_KbdType> getXhtml_kbdtypes() {
        return xhtml_kbdtypes;
    }

    public void addXhtml_kbdtype(Xhtml_kbdtype xhtml_kbdtype) {
        this.xhtml_kbdtypes.add(xhtml_kbdtype);
    }
    public List<xhtml_EmType> getXhtml_emtypes() {
        return xhtml_emtypes;
    }

    public void addXhtml_emtype(Xhtml_emtype xhtml_emtype) {
        this.xhtml_emtypes.add(xhtml_emtype);
    }
    public List<xhtml_SampType> getXhtml_samptypes() {
        return xhtml_samptypes;
    }

    public void addXhtml_samptype(Xhtml_samptype xhtml_samptype) {
        this.xhtml_samptypes.add(xhtml_samptype);
    }
    public List<xhtml_AcronymType> getXhtml_acronymtypes() {
        return xhtml_acronymtypes;
    }

    public void addXhtml_acronymtype(Xhtml_acronymtype xhtml_acronymtype) {
        this.xhtml_acronymtypes.add(xhtml_acronymtype);
    }
    public List<xhtml_DivType> getXhtml_divtypes() {
        return xhtml_divtypes;
    }

    public void addXhtml_divtype(Xhtml_divtype xhtml_divtype) {
        this.xhtml_divtypes.add(xhtml_divtype);
    }
    public List<xhtml_AddressType> getXhtml_addresstypes() {
        return xhtml_addresstypes;
    }

    public void addXhtml_addresstype(Xhtml_addresstype xhtml_addresstype) {
        this.xhtml_addresstypes.add(xhtml_addresstype);
    }
    public List<xhtml_SmallType> getXhtml_smalltypes() {
        return xhtml_smalltypes;
    }

    public void addXhtml_smalltype(Xhtml_smalltype xhtml_smalltype) {
        this.xhtml_smalltypes.add(xhtml_smalltype);
    }
    public List<xhtml_DelType> getXhtml_deltypes() {
        return xhtml_deltypes;
    }

    public void addXhtml_deltype(Xhtml_deltype xhtml_deltype) {
        this.xhtml_deltypes.add(xhtml_deltype);
    }
    public List<xhtml_StrongType> getXhtml_strongtypes() {
        return xhtml_strongtypes;
    }

    public void addXhtml_strongtype(Xhtml_strongtype xhtml_strongtype) {
        this.xhtml_strongtypes.add(xhtml_strongtype);
    }
    public List<xhtml_H6Type> getXhtml_h6types() {
        return xhtml_h6types;
    }

    public void addXhtml_h6type(Xhtml_h6type xhtml_h6type) {
        this.xhtml_h6types.add(xhtml_h6type);
    }
    public List<xhtml_BrType> getXhtml_brtypes() {
        return xhtml_brtypes;
    }

    public void addXhtml_brtype(Xhtml_brtype xhtml_brtype) {
        this.xhtml_brtypes.add(xhtml_brtype);
    }
    public List<xhtml_BlockquoteType> getXhtml_blockquotetypes() {
        return xhtml_blockquotetypes;
    }

    public void addXhtml_blockquotetype(Xhtml_blockquotetype xhtml_blockquotetype) {
        this.xhtml_blockquotetypes.add(xhtml_blockquotetype);
    }
    public List<xhtml_AbbrType> getXhtml_abbrtypes() {
        return xhtml_abbrtypes;
    }

    public void addXhtml_abbrtype(Xhtml_abbrtype xhtml_abbrtype) {
        this.xhtml_abbrtypes.add(xhtml_abbrtype);
    }
    public List<xhtml_BigType> getXhtml_bigtypes() {
        return xhtml_bigtypes;
    }

    public void addXhtml_bigtype(Xhtml_bigtype xhtml_bigtype) {
        this.xhtml_bigtypes.add(xhtml_bigtype);
    }
    public List<xhtml_SupType> getXhtml_suptypes() {
        return xhtml_suptypes;
    }

    public void addXhtml_suptype(Xhtml_suptype xhtml_suptype) {
        this.xhtml_suptypes.add(xhtml_suptype);
    }
    public List<xhtml_SpanType> getXhtml_spantypes() {
        return xhtml_spantypes;
    }

    public void addXhtml_spantype(Xhtml_spantype xhtml_spantype) {
        this.xhtml_spantypes.add(xhtml_spantype);
    }
    public List<xhtml_H5Type> getXhtml_h5types() {
        return xhtml_h5types;
    }

    public void addXhtml_h5type(Xhtml_h5type xhtml_h5type) {
        this.xhtml_h5types.add(xhtml_h5type);
    }
    public List<xhtml_UType> getXhtml_utypes() {
        return xhtml_utypes;
    }

    public void addXhtml_utype(Xhtml_utype xhtml_utype) {
        this.xhtml_utypes.add(xhtml_utype);
    }

}