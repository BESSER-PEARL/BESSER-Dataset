





import java.util.List;
import java.util.ArrayList;

public class uma_Role extends ContentElement {

    private String group2;
    private String responsibleFor;



    public uma_Role(
        String group2,        String responsibleFor    ) {
        super(
        );
        this.group2 = group2;
        this.responsibleFor = responsibleFor;
    }


    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getResponsiblefor() {
        return responsibleFor;
    }

    public void setResponsiblefor(String responsibleFor) {
        this.responsibleFor = responsibleFor;
    }


}