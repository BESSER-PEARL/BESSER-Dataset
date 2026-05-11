





import java.util.List;
import java.util.ArrayList;

public class rdpl_Column  {

    private String stype;
    private String ctype;
    private String name;





    private rdpl_Table rdpl_table;




    private rdpl_Type rdpl_type;




    private rdpl_ForeignKey rdpl_foreignkey;




    private rdpl_Table rdpl_table;


    public rdpl_Column(
        String stype,        String ctype,        String name    ) {
        this.stype = stype;
        this.ctype = ctype;
        this.name = name;
    }


    public String getStype() {
        return stype;
    }

    public void setStype(String stype) {
        this.stype = stype;
    }
    public String getCtype() {
        return ctype;
    }

    public void setCtype(String ctype) {
        this.ctype = ctype;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rdpl_Table getRdpl_table() {
        return rdpl_table;
    }

    public void setRdpl_table(rdpl_Table rdpl_table) {
        this.rdpl_table = rdpl_table;
    }
    public rdpl_Type getRdpl_type() {
        return rdpl_type;
    }

    public void setRdpl_type(rdpl_Type rdpl_type) {
        this.rdpl_type = rdpl_type;
    }
    public rdpl_ForeignKey getRdpl_foreignkey() {
        return rdpl_foreignkey;
    }

    public void setRdpl_foreignkey(rdpl_ForeignKey rdpl_foreignkey) {
        this.rdpl_foreignkey = rdpl_foreignkey;
    }
    public rdpl_Table getRdpl_table() {
        return rdpl_table;
    }

    public void setRdpl_table(rdpl_Table rdpl_table) {
        this.rdpl_table = rdpl_table;
    }

}