





import java.util.List;
import java.util.ArrayList;

public class contentfwk_OrganizationUnit extends Element {

    private String headcount;



    public contentfwk_OrganizationUnit(
        String headcount    ) {
        super(
        );
        this.headcount = headcount;
    }


    public String getHeadcount() {
        return headcount;
    }

    public void setHeadcount(String headcount) {
        this.headcount = headcount;
    }


}