





import java.util.List;
import java.util.ArrayList;

public class HTML_INPUT  {

    private String src;
    private String checked;
    private String maxlength;
    private String name;
    private String size;
    private String type;
    private String inputValue;
    private String align;



    public HTML_INPUT(
        String src,        String checked,        String maxlength,        String name,        String size,        String type,        String inputValue,        String align    ) {
        this.src = src;
        this.checked = checked;
        this.maxlength = maxlength;
        this.name = name;
        this.size = size;
        this.type = type;
        this.inputValue = inputValue;
        this.align = align;
    }


    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getChecked() {
        return checked;
    }

    public void setChecked(String checked) {
        this.checked = checked;
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
    public String getInputvalue() {
        return inputValue;
    }

    public void setInputvalue(String inputValue) {
        this.inputValue = inputValue;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }


}