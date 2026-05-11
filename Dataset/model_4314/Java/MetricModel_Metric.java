





import java.util.List;
import java.util.ArrayList;

public class MetricModel_Metric  {

    private String name;
    private String form;
    private String type;
    private String unit;
    private String id;
    private String description;



    public MetricModel_Metric(
        String name,        String form,        String type,        String unit,        String id,        String description    ) {
        this.name = name;
        this.form = form;
        this.type = type;
        this.unit = unit;
        this.id = id;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getForm() {
        return form;
    }

    public void setForm(String form) {
        this.form = form;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}