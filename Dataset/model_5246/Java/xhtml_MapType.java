





import java.util.List;
import java.util.ArrayList;

public class xhtml_MapType  {

    private String class_;
    private String title;
    private String block;
    private String name;
    private String lang;
    private String style;
    private String lang1;
    private String id;
    private String dir;





    private List<xhtml_AddressType> xhtml_addresstypes;




    private List<xhtml_PType> xhtml_ptypes;




    private List<xhtml_H5Type> xhtml_h5types;




    private List<xhtml_H3Type> xhtml_h3types;




    private List<xhtml_H6Type> xhtml_h6types;




    private xhtml_AContent xhtml_acontent;




    private List<xhtml_H1Type> xhtml_h1types;




    private List<xhtml_H2Type> xhtml_h2types;




    private List<xhtml_H4Type> xhtml_h4types;


    public xhtml_MapType(
        String class_,        String title,        String block,        String name,        String lang,        String style,        String lang1,        String id,        String dir    ) {
        this.class_ = class_;
        this.title = title;
        this.block = block;
        this.name = name;
        this.lang = lang;
        this.style = style;
        this.lang1 = lang1;
        this.id = id;
        this.dir = dir;
        this.xhtml_addresstypes = new ArrayList<>();
        this.xhtml_ptypes = new ArrayList<>();
        this.xhtml_h5types = new ArrayList<>();
        this.xhtml_h3types = new ArrayList<>();
        this.xhtml_h6types = new ArrayList<>();
        this.xhtml_h1types = new ArrayList<>();
        this.xhtml_h2types = new ArrayList<>();
        this.xhtml_h4types = new ArrayList<>();
    }

    public xhtml_MapType(
        String class_,        String title,        String block,        String name,        String lang,        String style,        String lang1,        String id,        String dir        ArrayList<xhtml_AddressType> xhtml_addresstypes,        ArrayList<xhtml_PType> xhtml_ptypes,        ArrayList<xhtml_H5Type> xhtml_h5types,        ArrayList<xhtml_H3Type> xhtml_h3types,        ArrayList<xhtml_H6Type> xhtml_h6types,        ArrayList<xhtml_H1Type> xhtml_h1types,        ArrayList<xhtml_H2Type> xhtml_h2types,        ArrayList<xhtml_H4Type> xhtml_h4types    ) {
        this.class_ = class_;
        this.title = title;
        this.block = block;
        this.name = name;
        this.lang = lang;
        this.style = style;
        this.lang1 = lang1;
        this.id = id;
        this.dir = dir;
        this.xhtml_addresstypes = xhtml_addresstypes;
        this.xhtml_ptypes = xhtml_ptypes;
        this.xhtml_h5types = xhtml_h5types;
        this.xhtml_h3types = xhtml_h3types;
        this.xhtml_h6types = xhtml_h6types;
        this.xhtml_h1types = xhtml_h1types;
        this.xhtml_h2types = xhtml_h2types;
        this.xhtml_h4types = xhtml_h4types;
    }

    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getBlock() {
        return block;
    }

    public void setBlock(String block) {
        this.block = block;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLang() {
        return lang;
    }

    public void setLang(String lang) {
        this.lang = lang;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getLang1() {
        return lang1;
    }

    public void setLang1(String lang1) {
        this.lang1 = lang1;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }

    public List<xhtml_AddressType> getXhtml_addresstypes() {
        return xhtml_addresstypes;
    }

    public void addXhtml_addresstype(Xhtml_addresstype xhtml_addresstype) {
        this.xhtml_addresstypes.add(xhtml_addresstype);
    }
    public List<xhtml_PType> getXhtml_ptypes() {
        return xhtml_ptypes;
    }

    public void addXhtml_ptype(Xhtml_ptype xhtml_ptype) {
        this.xhtml_ptypes.add(xhtml_ptype);
    }
    public List<xhtml_H5Type> getXhtml_h5types() {
        return xhtml_h5types;
    }

    public void addXhtml_h5type(Xhtml_h5type xhtml_h5type) {
        this.xhtml_h5types.add(xhtml_h5type);
    }
    public List<xhtml_H3Type> getXhtml_h3types() {
        return xhtml_h3types;
    }

    public void addXhtml_h3type(Xhtml_h3type xhtml_h3type) {
        this.xhtml_h3types.add(xhtml_h3type);
    }
    public List<xhtml_H6Type> getXhtml_h6types() {
        return xhtml_h6types;
    }

    public void addXhtml_h6type(Xhtml_h6type xhtml_h6type) {
        this.xhtml_h6types.add(xhtml_h6type);
    }
    public xhtml_AContent getXhtml_acontent() {
        return xhtml_acontent;
    }

    public void setXhtml_acontent(xhtml_AContent xhtml_acontent) {
        this.xhtml_acontent = xhtml_acontent;
    }
    public List<xhtml_H1Type> getXhtml_h1types() {
        return xhtml_h1types;
    }

    public void addXhtml_h1type(Xhtml_h1type xhtml_h1type) {
        this.xhtml_h1types.add(xhtml_h1type);
    }
    public List<xhtml_H2Type> getXhtml_h2types() {
        return xhtml_h2types;
    }

    public void addXhtml_h2type(Xhtml_h2type xhtml_h2type) {
        this.xhtml_h2types.add(xhtml_h2type);
    }
    public List<xhtml_H4Type> getXhtml_h4types() {
        return xhtml_h4types;
    }

    public void addXhtml_h4type(Xhtml_h4type xhtml_h4type) {
        this.xhtml_h4types.add(xhtml_h4type);
    }

}