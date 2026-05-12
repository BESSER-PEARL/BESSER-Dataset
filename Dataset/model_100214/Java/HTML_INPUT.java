





import java.util.List;
import java.util.ArrayList;

public class HTML_INPUT  {

    private String type;
    private String maxlength;
    private String inputValue;
    private String checked;
    private String align;
    private String name;
    private String src;
    private String size;



    public HTML_INPUT(
        String type,        String maxlength,        String inputValue,        String checked,        String align,        String name,        String src,        String size    ) {
        this.type = type;
        this.maxlength = maxlength;
        this.inputValue = inputValue;
        this.checked = checked;
        this.align = align;
        this.name = name;
        this.src = src;
        this.size = size;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getMaxlength() {
        return maxlength;
    }

    public void setMaxlength(String maxlength) {
        this.maxlength = maxlength;
    }
    public String getInputvalue() {
        return inputValue;
    }

    public void setInputvalue(String inputValue) {
        this.inputValue = inputValue;
    }
    public String getChecked() {
        return checked;
    }

    public void setChecked(String checked) {
        this.checked = checked;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }


}