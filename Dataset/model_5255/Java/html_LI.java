





import java.util.List;
import java.util.ArrayList;

public class html_LI extends ListElement {

    private String liValue;



    public html_LI(
        String liValue    ) {
        super(
        );
        this.liValue = liValue;
    }


    public String getLivalue() {
        return liValue;
    }

    public void setLivalue(String liValue) {
        this.liValue = liValue;
    }


}