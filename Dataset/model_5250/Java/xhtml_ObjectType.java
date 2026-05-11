





import java.util.List;
import java.util.ArrayList;

public class xhtml_ObjectType  {

    private String data;
    private String codebase;
    private String id;
    private String usemap;
    private String group;
    private String tabindex;
    private String type;
    private String declare;
    private String class_;
    private String style;
    private String mixed;
    private String title;
    private String height;
    private String standby;
    private String archive;
    private String width;
    private String classid;
    private String codetype;
    private String name;





    private List<xhtml_TtType> xhtml_tttypes;




    private List<xhtml_SampType> xhtml_samptypes;




    private List<xhtml_PType> xhtml_ptypes;




    private List<xhtml_H3Type> xhtml_h3types;




    private List<xhtml_H4Type> xhtml_h4types;




    private List<xhtml_IType> xhtml_itypes;




    private List<xhtml_UType> xhtml_utypes;




    private List<xhtml_SubType> xhtml_subtypes;




    private List<xhtml_VarType> xhtml_vartypes;




    private List<xhtml_BrType> xhtml_brtypes;




    private List<xhtml_H1Type> xhtml_h1types;




    private List<xhtml_SpanType> xhtml_spantypes;




    private xhtml_AContent xhtml_acontent;




    private List<xhtml_H6Type> xhtml_h6types;




    private List<xhtml_H2Type> xhtml_h2types;




    private List<xhtml_BType> xhtml_btypes;




    private List<xhtml_CodeType> xhtml_codetypes;




    private List<xhtml_BigType> xhtml_bigtypes;




    private List<xhtml_DfnType> xhtml_dfntypes;




    private List<xhtml_CiteType> xhtml_citetypes;




    private List<xhtml_AcronymType> xhtml_acronymtypes;




    private List<xhtml_StrikeType> xhtml_striketypes;




    private List<xhtml_SupType> xhtml_suptypes;




    private xhtml_ObjectType xhtml_objecttype;




    private List<xhtml_StrongType> xhtml_strongtypes;




    private List<xhtml_KbdType> xhtml_kbdtypes;




    private List<xhtml_SmallType> xhtml_smalltypes;




    private List<xhtml_H5Type> xhtml_h5types;




    private List<xhtml_AbbrType> xhtml_abbrtypes;




    private List<xhtml_AddressType> xhtml_addresstypes;




    private List<xhtml_QType> xhtml_qtypes;




    private List<xhtml_EmType> xhtml_emtypes;


    public xhtml_ObjectType(
        String data,        String codebase,        String id,        String usemap,        String group,        String tabindex,        String type,        String declare,        String class_,        String style,        String mixed,        String title,        String height,        String standby,        String archive,        String width,        String classid,        String codetype,        String name    ) {
        this.data = data;
        this.codebase = codebase;
        this.id = id;
        this.usemap = usemap;
        this.group = group;
        this.tabindex = tabindex;
        this.type = type;
        this.declare = declare;
        this.class_ = class_;
        this.style = style;
        this.mixed = mixed;
        this.title = title;
        this.height = height;
        this.standby = standby;
        this.archive = archive;
        this.width = width;
        this.classid = classid;
        this.codetype = codetype;
        this.name = name;
        this.xhtml_tttypes = new ArrayList<>();
        this.xhtml_samptypes = new ArrayList<>();
        this.xhtml_ptypes = new ArrayList<>();
        this.xhtml_h3types = new ArrayList<>();
        this.xhtml_h4types = new ArrayList<>();
        this.xhtml_itypes = new ArrayList<>();
        this.xhtml_utypes = new ArrayList<>();
        this.xhtml_subtypes = new ArrayList<>();
        this.xhtml_vartypes = new ArrayList<>();
        this.xhtml_brtypes = new ArrayList<>();
        this.xhtml_h1types = new ArrayList<>();
        this.xhtml_spantypes = new ArrayList<>();
        this.xhtml_h6types = new ArrayList<>();
        this.xhtml_h2types = new ArrayList<>();
        this.xhtml_btypes = new ArrayList<>();
        this.xhtml_codetypes = new ArrayList<>();
        this.xhtml_bigtypes = new ArrayList<>();
        this.xhtml_dfntypes = new ArrayList<>();
        this.xhtml_citetypes = new ArrayList<>();
        this.xhtml_acronymtypes = new ArrayList<>();
        this.xhtml_striketypes = new ArrayList<>();
        this.xhtml_suptypes = new ArrayList<>();
        this.xhtml_strongtypes = new ArrayList<>();
        this.xhtml_kbdtypes = new ArrayList<>();
        this.xhtml_smalltypes = new ArrayList<>();
        this.xhtml_h5types = new ArrayList<>();
        this.xhtml_abbrtypes = new ArrayList<>();
        this.xhtml_addresstypes = new ArrayList<>();
        this.xhtml_qtypes = new ArrayList<>();
        this.xhtml_emtypes = new ArrayList<>();
    }

    public xhtml_ObjectType(
        String data,        String codebase,        String id,        String usemap,        String group,        String tabindex,        String type,        String declare,        String class_,        String style,        String mixed,        String title,        String height,        String standby,        String archive,        String width,        String classid,        String codetype,        String name        ArrayList<xhtml_TtType> xhtml_tttypes,        ArrayList<xhtml_SampType> xhtml_samptypes,        ArrayList<xhtml_PType> xhtml_ptypes,        ArrayList<xhtml_H3Type> xhtml_h3types,        ArrayList<xhtml_H4Type> xhtml_h4types,        ArrayList<xhtml_IType> xhtml_itypes,        ArrayList<xhtml_UType> xhtml_utypes,        ArrayList<xhtml_SubType> xhtml_subtypes,        ArrayList<xhtml_VarType> xhtml_vartypes,        ArrayList<xhtml_BrType> xhtml_brtypes,        ArrayList<xhtml_H1Type> xhtml_h1types,        ArrayList<xhtml_SpanType> xhtml_spantypes,        ArrayList<xhtml_H6Type> xhtml_h6types,        ArrayList<xhtml_H2Type> xhtml_h2types,        ArrayList<xhtml_BType> xhtml_btypes,        ArrayList<xhtml_CodeType> xhtml_codetypes,        ArrayList<xhtml_BigType> xhtml_bigtypes,        ArrayList<xhtml_DfnType> xhtml_dfntypes,        ArrayList<xhtml_CiteType> xhtml_citetypes,        ArrayList<xhtml_AcronymType> xhtml_acronymtypes,        ArrayList<xhtml_StrikeType> xhtml_striketypes,        ArrayList<xhtml_SupType> xhtml_suptypes,        ArrayList<xhtml_StrongType> xhtml_strongtypes,        ArrayList<xhtml_KbdType> xhtml_kbdtypes,        ArrayList<xhtml_SmallType> xhtml_smalltypes,        ArrayList<xhtml_H5Type> xhtml_h5types,        ArrayList<xhtml_AbbrType> xhtml_abbrtypes,        ArrayList<xhtml_AddressType> xhtml_addresstypes,        ArrayList<xhtml_QType> xhtml_qtypes,        ArrayList<xhtml_EmType> xhtml_emtypes    ) {
        this.data = data;
        this.codebase = codebase;
        this.id = id;
        this.usemap = usemap;
        this.group = group;
        this.tabindex = tabindex;
        this.type = type;
        this.declare = declare;
        this.class_ = class_;
        this.style = style;
        this.mixed = mixed;
        this.title = title;
        this.height = height;
        this.standby = standby;
        this.archive = archive;
        this.width = width;
        this.classid = classid;
        this.codetype = codetype;
        this.name = name;
        this.xhtml_tttypes = xhtml_tttypes;
        this.xhtml_samptypes = xhtml_samptypes;
        this.xhtml_ptypes = xhtml_ptypes;
        this.xhtml_h3types = xhtml_h3types;
        this.xhtml_h4types = xhtml_h4types;
        this.xhtml_itypes = xhtml_itypes;
        this.xhtml_utypes = xhtml_utypes;
        this.xhtml_subtypes = xhtml_subtypes;
        this.xhtml_vartypes = xhtml_vartypes;
        this.xhtml_brtypes = xhtml_brtypes;
        this.xhtml_h1types = xhtml_h1types;
        this.xhtml_spantypes = xhtml_spantypes;
        this.xhtml_h6types = xhtml_h6types;
        this.xhtml_h2types = xhtml_h2types;
        this.xhtml_btypes = xhtml_btypes;
        this.xhtml_codetypes = xhtml_codetypes;
        this.xhtml_bigtypes = xhtml_bigtypes;
        this.xhtml_dfntypes = xhtml_dfntypes;
        this.xhtml_citetypes = xhtml_citetypes;
        this.xhtml_acronymtypes = xhtml_acronymtypes;
        this.xhtml_striketypes = xhtml_striketypes;
        this.xhtml_suptypes = xhtml_suptypes;
        this.xhtml_strongtypes = xhtml_strongtypes;
        this.xhtml_kbdtypes = xhtml_kbdtypes;
        this.xhtml_smalltypes = xhtml_smalltypes;
        this.xhtml_h5types = xhtml_h5types;
        this.xhtml_abbrtypes = xhtml_abbrtypes;
        this.xhtml_addresstypes = xhtml_addresstypes;
        this.xhtml_qtypes = xhtml_qtypes;
        this.xhtml_emtypes = xhtml_emtypes;
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getCodebase() {
        return codebase;
    }

    public void setCodebase(String codebase) {
        this.codebase = codebase;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getUsemap() {
        return usemap;
    }

    public void setUsemap(String usemap) {
        this.usemap = usemap;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getTabindex() {
        return tabindex;
    }

    public void setTabindex(String tabindex) {
        this.tabindex = tabindex;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDeclare() {
        return declare;
    }

    public void setDeclare(String declare) {
        this.declare = declare;
    }
    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getStandby() {
        return standby;
    }

    public void setStandby(String standby) {
        this.standby = standby;
    }
    public String getArchive() {
        return archive;
    }

    public void setArchive(String archive) {
        this.archive = archive;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getClassid() {
        return classid;
    }

    public void setClassid(String classid) {
        this.classid = classid;
    }
    public String getCodetype() {
        return codetype;
    }

    public void setCodetype(String codetype) {
        this.codetype = codetype;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<xhtml_TtType> getXhtml_tttypes() {
        return xhtml_tttypes;
    }

    public void addXhtml_tttype(Xhtml_tttype xhtml_tttype) {
        this.xhtml_tttypes.add(xhtml_tttype);
    }
    public List<xhtml_SampType> getXhtml_samptypes() {
        return xhtml_samptypes;
    }

    public void addXhtml_samptype(Xhtml_samptype xhtml_samptype) {
        this.xhtml_samptypes.add(xhtml_samptype);
    }
    public List<xhtml_PType> getXhtml_ptypes() {
        return xhtml_ptypes;
    }

    public void addXhtml_ptype(Xhtml_ptype xhtml_ptype) {
        this.xhtml_ptypes.add(xhtml_ptype);
    }
    public List<xhtml_H3Type> getXhtml_h3types() {
        return xhtml_h3types;
    }

    public void addXhtml_h3type(Xhtml_h3type xhtml_h3type) {
        this.xhtml_h3types.add(xhtml_h3type);
    }
    public List<xhtml_H4Type> getXhtml_h4types() {
        return xhtml_h4types;
    }

    public void addXhtml_h4type(Xhtml_h4type xhtml_h4type) {
        this.xhtml_h4types.add(xhtml_h4type);
    }
    public List<xhtml_IType> getXhtml_itypes() {
        return xhtml_itypes;
    }

    public void addXhtml_itype(Xhtml_itype xhtml_itype) {
        this.xhtml_itypes.add(xhtml_itype);
    }
    public List<xhtml_UType> getXhtml_utypes() {
        return xhtml_utypes;
    }

    public void addXhtml_utype(Xhtml_utype xhtml_utype) {
        this.xhtml_utypes.add(xhtml_utype);
    }
    public List<xhtml_SubType> getXhtml_subtypes() {
        return xhtml_subtypes;
    }

    public void addXhtml_subtype(Xhtml_subtype xhtml_subtype) {
        this.xhtml_subtypes.add(xhtml_subtype);
    }
    public List<xhtml_VarType> getXhtml_vartypes() {
        return xhtml_vartypes;
    }

    public void addXhtml_vartype(Xhtml_vartype xhtml_vartype) {
        this.xhtml_vartypes.add(xhtml_vartype);
    }
    public List<xhtml_BrType> getXhtml_brtypes() {
        return xhtml_brtypes;
    }

    public void addXhtml_brtype(Xhtml_brtype xhtml_brtype) {
        this.xhtml_brtypes.add(xhtml_brtype);
    }
    public List<xhtml_H1Type> getXhtml_h1types() {
        return xhtml_h1types;
    }

    public void addXhtml_h1type(Xhtml_h1type xhtml_h1type) {
        this.xhtml_h1types.add(xhtml_h1type);
    }
    public List<xhtml_SpanType> getXhtml_spantypes() {
        return xhtml_spantypes;
    }

    public void addXhtml_spantype(Xhtml_spantype xhtml_spantype) {
        this.xhtml_spantypes.add(xhtml_spantype);
    }
    public xhtml_AContent getXhtml_acontent() {
        return xhtml_acontent;
    }

    public void setXhtml_acontent(xhtml_AContent xhtml_acontent) {
        this.xhtml_acontent = xhtml_acontent;
    }
    public List<xhtml_H6Type> getXhtml_h6types() {
        return xhtml_h6types;
    }

    public void addXhtml_h6type(Xhtml_h6type xhtml_h6type) {
        this.xhtml_h6types.add(xhtml_h6type);
    }
    public List<xhtml_H2Type> getXhtml_h2types() {
        return xhtml_h2types;
    }

    public void addXhtml_h2type(Xhtml_h2type xhtml_h2type) {
        this.xhtml_h2types.add(xhtml_h2type);
    }
    public List<xhtml_BType> getXhtml_btypes() {
        return xhtml_btypes;
    }

    public void addXhtml_btype(Xhtml_btype xhtml_btype) {
        this.xhtml_btypes.add(xhtml_btype);
    }
    public List<xhtml_CodeType> getXhtml_codetypes() {
        return xhtml_codetypes;
    }

    public void addXhtml_codetype(Xhtml_codetype xhtml_codetype) {
        this.xhtml_codetypes.add(xhtml_codetype);
    }
    public List<xhtml_BigType> getXhtml_bigtypes() {
        return xhtml_bigtypes;
    }

    public void addXhtml_bigtype(Xhtml_bigtype xhtml_bigtype) {
        this.xhtml_bigtypes.add(xhtml_bigtype);
    }
    public List<xhtml_DfnType> getXhtml_dfntypes() {
        return xhtml_dfntypes;
    }

    public void addXhtml_dfntype(Xhtml_dfntype xhtml_dfntype) {
        this.xhtml_dfntypes.add(xhtml_dfntype);
    }
    public List<xhtml_CiteType> getXhtml_citetypes() {
        return xhtml_citetypes;
    }

    public void addXhtml_citetype(Xhtml_citetype xhtml_citetype) {
        this.xhtml_citetypes.add(xhtml_citetype);
    }
    public List<xhtml_AcronymType> getXhtml_acronymtypes() {
        return xhtml_acronymtypes;
    }

    public void addXhtml_acronymtype(Xhtml_acronymtype xhtml_acronymtype) {
        this.xhtml_acronymtypes.add(xhtml_acronymtype);
    }
    public List<xhtml_StrikeType> getXhtml_striketypes() {
        return xhtml_striketypes;
    }

    public void addXhtml_striketype(Xhtml_striketype xhtml_striketype) {
        this.xhtml_striketypes.add(xhtml_striketype);
    }
    public List<xhtml_SupType> getXhtml_suptypes() {
        return xhtml_suptypes;
    }

    public void addXhtml_suptype(Xhtml_suptype xhtml_suptype) {
        this.xhtml_suptypes.add(xhtml_suptype);
    }
    public xhtml_ObjectType getXhtml_objecttype() {
        return xhtml_objecttype;
    }

    public void setXhtml_objecttype(xhtml_ObjectType xhtml_objecttype) {
        this.xhtml_objecttype = xhtml_objecttype;
    }
    public List<xhtml_StrongType> getXhtml_strongtypes() {
        return xhtml_strongtypes;
    }

    public void addXhtml_strongtype(Xhtml_strongtype xhtml_strongtype) {
        this.xhtml_strongtypes.add(xhtml_strongtype);
    }
    public List<xhtml_KbdType> getXhtml_kbdtypes() {
        return xhtml_kbdtypes;
    }

    public void addXhtml_kbdtype(Xhtml_kbdtype xhtml_kbdtype) {
        this.xhtml_kbdtypes.add(xhtml_kbdtype);
    }
    public List<xhtml_SmallType> getXhtml_smalltypes() {
        return xhtml_smalltypes;
    }

    public void addXhtml_smalltype(Xhtml_smalltype xhtml_smalltype) {
        this.xhtml_smalltypes.add(xhtml_smalltype);
    }
    public List<xhtml_H5Type> getXhtml_h5types() {
        return xhtml_h5types;
    }

    public void addXhtml_h5type(Xhtml_h5type xhtml_h5type) {
        this.xhtml_h5types.add(xhtml_h5type);
    }
    public List<xhtml_AbbrType> getXhtml_abbrtypes() {
        return xhtml_abbrtypes;
    }

    public void addXhtml_abbrtype(Xhtml_abbrtype xhtml_abbrtype) {
        this.xhtml_abbrtypes.add(xhtml_abbrtype);
    }
    public List<xhtml_AddressType> getXhtml_addresstypes() {
        return xhtml_addresstypes;
    }

    public void addXhtml_addresstype(Xhtml_addresstype xhtml_addresstype) {
        this.xhtml_addresstypes.add(xhtml_addresstype);
    }
    public List<xhtml_QType> getXhtml_qtypes() {
        return xhtml_qtypes;
    }

    public void addXhtml_qtype(Xhtml_qtype xhtml_qtype) {
        this.xhtml_qtypes.add(xhtml_qtype);
    }
    public List<xhtml_EmType> getXhtml_emtypes() {
        return xhtml_emtypes;
    }

    public void addXhtml_emtype(Xhtml_emtype xhtml_emtype) {
        this.xhtml_emtypes.add(xhtml_emtype);
    }

}