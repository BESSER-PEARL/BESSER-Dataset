





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_IntoClause  {

    private String descriptorName;
    private String using;



    public syntax_dbl_IntoClause(
        String descriptorName,        String using    ) {
        this.descriptorName = descriptorName;
        this.using = using;
    }


    public String getDescriptorname() {
        return descriptorName;
    }

    public void setDescriptorname(String descriptorName) {
        this.descriptorName = descriptorName;
    }
    public String getUsing() {
        return using;
    }

    public void setUsing(String using) {
        this.using = using;
    }


}