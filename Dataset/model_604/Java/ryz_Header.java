





import java.util.List;
import java.util.ArrayList;

public class ryz_Header  {

    private String name;
    private String labelText;





    private ryz_Table ryz_table;


    public ryz_Header(
        String name,        String labelText    ) {
        this.name = name;
        this.labelText = labelText;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLabeltext() {
        return labelText;
    }

    public void setLabeltext(String labelText) {
        this.labelText = labelText;
    }

    public ryz_Table getRyz_table() {
        return ryz_table;
    }

    public void setRyz_table(ryz_Table ryz_table) {
        this.ryz_table = ryz_table;
    }

}