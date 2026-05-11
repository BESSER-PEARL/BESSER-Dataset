





import java.util.List;
import java.util.ArrayList;

public class SPL_WhenHeader extends VariableDeclaration {

    private String headerId;





    private SPL_Constant spl_constant;


    public SPL_WhenHeader(
        String headerId    ) {
        super(
        );
        this.headerId = headerId;
    }


    public String getHeaderid() {
        return headerId;
    }

    public void setHeaderid(String headerId) {
        this.headerId = headerId;
    }

    public SPL_Constant getSpl_constant() {
        return spl_constant;
    }

    public void setSpl_constant(SPL_Constant spl_constant) {
        this.spl_constant = spl_constant;
    }

}