





import java.util.List;
import java.util.ArrayList;

public class vhdl_RecordField  {

    private String name;





    private vhdl_Member vhdl_member;


    public vhdl_RecordField(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public vhdl_Member getVhdl_member() {
        return vhdl_member;
    }

    public void setVhdl_member(vhdl_Member vhdl_member) {
        this.vhdl_member = vhdl_member;
    }

}