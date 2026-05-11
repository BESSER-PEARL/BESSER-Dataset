





import java.util.List;
import java.util.ArrayList;

public class xhtml_FormContent  {

    private String group;





    private List<xhtml_H4Type> xhtml_h4types;




    private List<xhtml_AddressType> xhtml_addresstypes;




    private List<xhtml_PType> xhtml_ptypes;




    private List<xhtml_H5Type> xhtml_h5types;




    private List<xhtml_InsType> xhtml_instypes;




    private List<xhtml_DlType> xhtml_dltypes;




    private List<xhtml_H2Type> xhtml_h2types;




    private List<xhtml_DelType> xhtml_deltypes;




    private List<xhtml_H1Type> xhtml_h1types;




    private List<xhtml_HrType> xhtml_hrtypes;




    private List<xhtml_BlockquoteType> xhtml_blockquotetypes;




    private List<xhtml_H3Type> xhtml_h3types;




    private List<xhtml_DivType> xhtml_divtypes;




    private List<xhtml_UlType> xhtml_ultypes;




    private List<xhtml_TableType> xhtml_tabletypes;




    private List<xhtml_PreType> xhtml_pretypes;




    private List<xhtml_H6Type> xhtml_h6types;




    private List<xhtml_OlType> xhtml_oltypes;


    public xhtml_FormContent(
        String group    ) {
        this.group = group;
        this.xhtml_h4types = new ArrayList<>();
        this.xhtml_addresstypes = new ArrayList<>();
        this.xhtml_ptypes = new ArrayList<>();
        this.xhtml_h5types = new ArrayList<>();
        this.xhtml_instypes = new ArrayList<>();
        this.xhtml_dltypes = new ArrayList<>();
        this.xhtml_h2types = new ArrayList<>();
        this.xhtml_deltypes = new ArrayList<>();
        this.xhtml_h1types = new ArrayList<>();
        this.xhtml_hrtypes = new ArrayList<>();
        this.xhtml_blockquotetypes = new ArrayList<>();
        this.xhtml_h3types = new ArrayList<>();
        this.xhtml_divtypes = new ArrayList<>();
        this.xhtml_ultypes = new ArrayList<>();
        this.xhtml_tabletypes = new ArrayList<>();
        this.xhtml_pretypes = new ArrayList<>();
        this.xhtml_h6types = new ArrayList<>();
        this.xhtml_oltypes = new ArrayList<>();
    }

    public xhtml_FormContent(
        String group        ArrayList<xhtml_H4Type> xhtml_h4types,        ArrayList<xhtml_AddressType> xhtml_addresstypes,        ArrayList<xhtml_PType> xhtml_ptypes,        ArrayList<xhtml_H5Type> xhtml_h5types,        ArrayList<xhtml_InsType> xhtml_instypes,        ArrayList<xhtml_DlType> xhtml_dltypes,        ArrayList<xhtml_H2Type> xhtml_h2types,        ArrayList<xhtml_DelType> xhtml_deltypes,        ArrayList<xhtml_H1Type> xhtml_h1types,        ArrayList<xhtml_HrType> xhtml_hrtypes,        ArrayList<xhtml_BlockquoteType> xhtml_blockquotetypes,        ArrayList<xhtml_H3Type> xhtml_h3types,        ArrayList<xhtml_DivType> xhtml_divtypes,        ArrayList<xhtml_UlType> xhtml_ultypes,        ArrayList<xhtml_TableType> xhtml_tabletypes,        ArrayList<xhtml_PreType> xhtml_pretypes,        ArrayList<xhtml_H6Type> xhtml_h6types,        ArrayList<xhtml_OlType> xhtml_oltypes    ) {
        this.group = group;
        this.xhtml_h4types = xhtml_h4types;
        this.xhtml_addresstypes = xhtml_addresstypes;
        this.xhtml_ptypes = xhtml_ptypes;
        this.xhtml_h5types = xhtml_h5types;
        this.xhtml_instypes = xhtml_instypes;
        this.xhtml_dltypes = xhtml_dltypes;
        this.xhtml_h2types = xhtml_h2types;
        this.xhtml_deltypes = xhtml_deltypes;
        this.xhtml_h1types = xhtml_h1types;
        this.xhtml_hrtypes = xhtml_hrtypes;
        this.xhtml_blockquotetypes = xhtml_blockquotetypes;
        this.xhtml_h3types = xhtml_h3types;
        this.xhtml_divtypes = xhtml_divtypes;
        this.xhtml_ultypes = xhtml_ultypes;
        this.xhtml_tabletypes = xhtml_tabletypes;
        this.xhtml_pretypes = xhtml_pretypes;
        this.xhtml_h6types = xhtml_h6types;
        this.xhtml_oltypes = xhtml_oltypes;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<xhtml_H4Type> getXhtml_h4types() {
        return xhtml_h4types;
    }

    public void addXhtml_h4type(Xhtml_h4type xhtml_h4type) {
        this.xhtml_h4types.add(xhtml_h4type);
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
    public List<xhtml_InsType> getXhtml_instypes() {
        return xhtml_instypes;
    }

    public void addXhtml_instype(Xhtml_instype xhtml_instype) {
        this.xhtml_instypes.add(xhtml_instype);
    }
    public List<xhtml_DlType> getXhtml_dltypes() {
        return xhtml_dltypes;
    }

    public void addXhtml_dltype(Xhtml_dltype xhtml_dltype) {
        this.xhtml_dltypes.add(xhtml_dltype);
    }
    public List<xhtml_H2Type> getXhtml_h2types() {
        return xhtml_h2types;
    }

    public void addXhtml_h2type(Xhtml_h2type xhtml_h2type) {
        this.xhtml_h2types.add(xhtml_h2type);
    }
    public List<xhtml_DelType> getXhtml_deltypes() {
        return xhtml_deltypes;
    }

    public void addXhtml_deltype(Xhtml_deltype xhtml_deltype) {
        this.xhtml_deltypes.add(xhtml_deltype);
    }
    public List<xhtml_H1Type> getXhtml_h1types() {
        return xhtml_h1types;
    }

    public void addXhtml_h1type(Xhtml_h1type xhtml_h1type) {
        this.xhtml_h1types.add(xhtml_h1type);
    }
    public List<xhtml_HrType> getXhtml_hrtypes() {
        return xhtml_hrtypes;
    }

    public void addXhtml_hrtype(Xhtml_hrtype xhtml_hrtype) {
        this.xhtml_hrtypes.add(xhtml_hrtype);
    }
    public List<xhtml_BlockquoteType> getXhtml_blockquotetypes() {
        return xhtml_blockquotetypes;
    }

    public void addXhtml_blockquotetype(Xhtml_blockquotetype xhtml_blockquotetype) {
        this.xhtml_blockquotetypes.add(xhtml_blockquotetype);
    }
    public List<xhtml_H3Type> getXhtml_h3types() {
        return xhtml_h3types;
    }

    public void addXhtml_h3type(Xhtml_h3type xhtml_h3type) {
        this.xhtml_h3types.add(xhtml_h3type);
    }
    public List<xhtml_DivType> getXhtml_divtypes() {
        return xhtml_divtypes;
    }

    public void addXhtml_divtype(Xhtml_divtype xhtml_divtype) {
        this.xhtml_divtypes.add(xhtml_divtype);
    }
    public List<xhtml_UlType> getXhtml_ultypes() {
        return xhtml_ultypes;
    }

    public void addXhtml_ultype(Xhtml_ultype xhtml_ultype) {
        this.xhtml_ultypes.add(xhtml_ultype);
    }
    public List<xhtml_TableType> getXhtml_tabletypes() {
        return xhtml_tabletypes;
    }

    public void addXhtml_tabletype(Xhtml_tabletype xhtml_tabletype) {
        this.xhtml_tabletypes.add(xhtml_tabletype);
    }
    public List<xhtml_PreType> getXhtml_pretypes() {
        return xhtml_pretypes;
    }

    public void addXhtml_pretype(Xhtml_pretype xhtml_pretype) {
        this.xhtml_pretypes.add(xhtml_pretype);
    }
    public List<xhtml_H6Type> getXhtml_h6types() {
        return xhtml_h6types;
    }

    public void addXhtml_h6type(Xhtml_h6type xhtml_h6type) {
        this.xhtml_h6types.add(xhtml_h6type);
    }
    public List<xhtml_OlType> getXhtml_oltypes() {
        return xhtml_oltypes;
    }

    public void addXhtml_oltype(Xhtml_oltype xhtml_oltype) {
        this.xhtml_oltypes.add(xhtml_oltype);
    }

}