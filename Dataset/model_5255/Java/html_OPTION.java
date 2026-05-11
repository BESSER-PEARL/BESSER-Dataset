





import java.util.List;
import java.util.ArrayList;

public class html_OPTION  {

    private String optionValue;
    private String selected;



    public html_OPTION(
        String optionValue,        String selected    ) {
        this.optionValue = optionValue;
        this.selected = selected;
    }


    public String getOptionvalue() {
        return optionValue;
    }

    public void setOptionvalue(String optionValue) {
        this.optionValue = optionValue;
    }
    public String getSelected() {
        return selected;
    }

    public void setSelected(String selected) {
        this.selected = selected;
    }


}