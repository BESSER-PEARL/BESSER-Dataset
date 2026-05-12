





import java.util.List;
import java.util.ArrayList;

public class HTML_INPUT  {

    private String src;
    private String maxlength;
    private String name;
    private String align;
    private String size;
    private String type;
    private String checked;
    private String inputValue;



    public HTML_INPUT(
        String src,        String maxlength,        String name,        String align,        String size,        String type,        String checked,        String inputValue    ) {
        this.src = src;
        this.maxlength = maxlength;
        this.name = name;
        this.align = align;
        this.size = size;
        this.type = type;
        this.checked = checked;
        this.inputValue = inputValue;
    }


    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getMaxlength() {
        return maxlength;
    }

    public void setMaxlength(String maxlength) {
        this.maxlength = maxlength;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getChecked() {
        return checked;
    }

    public void setChecked(String checked) {
        this.checked = checked;
    }
    public String getInputvalue() {
        return inputValue;
    }

    public void setInputvalue(String inputValue) {
        this.inputValue = inputValue;
    }


}