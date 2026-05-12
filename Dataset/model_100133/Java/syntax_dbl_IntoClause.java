





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_IntoClause  {

    private String using;
    private String descriptorName;



    public syntax_dbl_IntoClause(
        String using,        String descriptorName    ) {
        this.using = using;
        this.descriptorName = descriptorName;
    }


    public String getUsing() {
        return using;
    }

    public void setUsing(String using) {
        this.using = using;
    }
    public String getDescriptorname() {
        return descriptorName;
    }

    public void setDescriptorname(String descriptorName) {
        this.descriptorName = descriptorName;
    }


}