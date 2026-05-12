





import java.util.List;
import java.util.ArrayList;

public class HTML_INPUT  {

    private String name;
    private String checked;
    private String type;
    private String inputValue;
    private String maxlength;
    private String src;
    private String align;
    private String size;



    public HTML_INPUT(
        String name,        String checked,        String type,        String inputValue,        String maxlength,        String src,        String align,        String size    ) {
        this.name = name;
        this.checked = checked;
        this.type = type;
        this.inputValue = inputValue;
        this.maxlength = maxlength;
        this.src = src;
        this.align = align;
        this.size = size;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getChecked() {
        return checked;
    }

    public void setChecked(String checked) {
        this.checked = checked;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getInputvalue() {
        return inputValue;
    }

    public void setInputvalue(String inputValue) {
        this.inputValue = inputValue;
    }
    public String getMaxlength() {
        return maxlength;
    }

    public void setMaxlength(String maxlength) {
        this.maxlength = maxlength;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }


}