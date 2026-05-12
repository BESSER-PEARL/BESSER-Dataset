





import java.util.List;
import java.util.ArrayList;

public class HTML_INPUT  {

    private String inputValue;
    private String align;
    private String checked;
    private String size;
    private String name;
    private String src;
    private String type;
    private String maxlength;



    public HTML_INPUT(
        String inputValue,        String align,        String checked,        String size,        String name,        String src,        String type,        String maxlength    ) {
        this.inputValue = inputValue;
        this.align = align;
        this.checked = checked;
        this.size = size;
        this.name = name;
        this.src = src;
        this.type = type;
        this.maxlength = maxlength;
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
    public String getChecked() {
        return checked;
    }

    public void setChecked(String checked) {
        this.checked = checked;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
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


}