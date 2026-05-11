





import java.util.List;
import java.util.ArrayList;

public class model_CEFACTCode extends IEntity {

    private String name_de;
    private String code;
    private String abbreviation_en;
    private String target;
    private String abbreviation_de;



    public model_CEFACTCode(
        String name_de,        String code,        String abbreviation_en,        String target,        String abbreviation_de    ) {
        super(
        );
        this.name_de = name_de;
        this.code = code;
        this.abbreviation_en = abbreviation_en;
        this.target = target;
        this.abbreviation_de = abbreviation_de;
    }


    public String getName_de() {
        return name_de;
    }

    public void setName_de(String name_de) {
        this.name_de = name_de;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getAbbreviation_en() {
        return abbreviation_en;
    }

    public void setAbbreviation_en(String abbreviation_en) {
        this.abbreviation_en = abbreviation_en;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getAbbreviation_de() {
        return abbreviation_de;
    }

    public void setAbbreviation_de(String abbreviation_de) {
        this.abbreviation_de = abbreviation_de;
    }


}