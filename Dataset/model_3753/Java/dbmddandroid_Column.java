





import java.util.List;
import java.util.ArrayList;

public class dbmddandroid_Column extends NamedElement {

    private String type;



    public dbmddandroid_Column(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}