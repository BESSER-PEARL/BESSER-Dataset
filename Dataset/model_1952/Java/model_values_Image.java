





import java.util.List;
import java.util.ArrayList;

public class model_values_Image extends Value {

    private String name;
    private String data;
    private String format;
    private String reference;



    public model_values_Image(
        String name,        String data,        String format,        String reference    ) {
        super(
        );
        this.name = name;
        this.data = data;
        this.format = format;
        this.reference = reference;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }
    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }


}