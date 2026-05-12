





import java.util.List;
import java.util.ArrayList;

public class HTML_OPTION  {

    private String selected;
    private String optionValue;



    public HTML_OPTION(
        String selected,        String optionValue    ) {
        this.selected = selected;
        this.optionValue = optionValue;
    }


    public String getSelected() {
        return selected;
    }

    public void setSelected(String selected) {
        this.selected = selected;
    }
    public String getOptionvalue() {
        return optionValue;
    }

    public void setOptionvalue(String optionValue) {
        this.optionValue = optionValue;
    }


}