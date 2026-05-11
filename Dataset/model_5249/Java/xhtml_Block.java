





import java.util.List;
import java.util.ArrayList;

public class xhtml_Block  {

    private String group;





    private List<xhtml_InsType> xhtml_instypes;




    private List<xhtml_PType> xhtml_ptypes;




    private List<xhtml_H4Type> xhtml_h4types;




    private List<xhtml_AddressType> xhtml_addresstypes;




    private List<xhtml_H6Type> xhtml_h6types;




    private List<xhtml_H3Type> xhtml_h3types;




    private List<xhtml_H2Type> xhtml_h2types;




    private List<xhtml_DelType> xhtml_deltypes;




    private List<xhtml_H1Type> xhtml_h1types;




    private List<xhtml_H5Type> xhtml_h5types;


    public xhtml_Block(
        String group    ) {
        this.group = group;
        this.xhtml_instypes = new ArrayList<>();
        this.xhtml_ptypes = new ArrayList<>();
        this.xhtml_h4types = new ArrayList<>();
        this.xhtml_addresstypes = new ArrayList<>();
        this.xhtml_h6types = new ArrayList<>();
        this.xhtml_h3types = new ArrayList<>();
        this.xhtml_h2types = new ArrayList<>();
        this.xhtml_deltypes = new ArrayList<>();
        this.xhtml_h1types = new ArrayList<>();
        this.xhtml_h5types = new ArrayList<>();
    }

    public xhtml_Block(
        String group        ArrayList<xhtml_InsType> xhtml_instypes,        ArrayList<xhtml_PType> xhtml_ptypes,        ArrayList<xhtml_H4Type> xhtml_h4types,        ArrayList<xhtml_AddressType> xhtml_addresstypes,        ArrayList<xhtml_H6Type> xhtml_h6types,        ArrayList<xhtml_H3Type> xhtml_h3types,        ArrayList<xhtml_H2Type> xhtml_h2types,        ArrayList<xhtml_DelType> xhtml_deltypes,        ArrayList<xhtml_H1Type> xhtml_h1types,        ArrayList<xhtml_H5Type> xhtml_h5types    ) {
        this.group = group;
        this.xhtml_instypes = xhtml_instypes;
        this.xhtml_ptypes = xhtml_ptypes;
        this.xhtml_h4types = xhtml_h4types;
        this.xhtml_addresstypes = xhtml_addresstypes;
        this.xhtml_h6types = xhtml_h6types;
        this.xhtml_h3types = xhtml_h3types;
        this.xhtml_h2types = xhtml_h2types;
        this.xhtml_deltypes = xhtml_deltypes;
        this.xhtml_h1types = xhtml_h1types;
        this.xhtml_h5types = xhtml_h5types;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<xhtml_InsType> getXhtml_instypes() {
        return xhtml_instypes;
    }

    public void addXhtml_instype(Xhtml_instype xhtml_instype) {
        this.xhtml_instypes.add(xhtml_instype);
    }
    public List<xhtml_PType> getXhtml_ptypes() {
        return xhtml_ptypes;
    }

    public void addXhtml_ptype(Xhtml_ptype xhtml_ptype) {
        this.xhtml_ptypes.add(xhtml_ptype);
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
    public List<xhtml_H6Type> getXhtml_h6types() {
        return xhtml_h6types;
    }

    public void addXhtml_h6type(Xhtml_h6type xhtml_h6type) {
        this.xhtml_h6types.add(xhtml_h6type);
    }
    public List<xhtml_H3Type> getXhtml_h3types() {
        return xhtml_h3types;
    }

    public void addXhtml_h3type(Xhtml_h3type xhtml_h3type) {
        this.xhtml_h3types.add(xhtml_h3type);
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
    public List<xhtml_H5Type> getXhtml_h5types() {
        return xhtml_h5types;
    }

    public void addXhtml_h5type(Xhtml_h5type xhtml_h5type) {
        this.xhtml_h5types.add(xhtml_h5type);
    }

}