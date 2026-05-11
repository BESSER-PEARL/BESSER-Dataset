





import java.util.List;
import java.util.ArrayList;

public class multicontainment_b_ChildB2 extends Identified {

    private String name;





    private multicontainment_b_RootB multicontainment_b_rootb;


    public multicontainment_b_ChildB2(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public multicontainment_b_RootB getMulticontainment_b_rootb() {
        return multicontainment_b_rootb;
    }

    public void setMulticontainment_b_rootb(multicontainment_b_RootB multicontainment_b_rootb) {
        this.multicontainment_b_rootb = multicontainment_b_rootb;
    }

}