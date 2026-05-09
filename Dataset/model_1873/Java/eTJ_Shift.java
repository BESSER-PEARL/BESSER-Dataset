





import java.util.List;
import java.util.ArrayList;

public class eTJ_Shift extends Property {

    private String id;
    private String name;
    private String replace;
    private String timezone;





    private eTJ_Shift etj_shift;


    public eTJ_Shift(
        String id,        String name,        String replace,        String timezone    ) {
        super(
        );
        this.id = id;
        this.name = name;
        this.replace = replace;
        this.timezone = timezone;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getReplace() {
        return replace;
    }

    public void setReplace(String replace) {
        this.replace = replace;
    }
    public String getTimezone() {
        return timezone;
    }

    public void setTimezone(String timezone) {
        this.timezone = timezone;
    }

    public eTJ_Shift getEtj_shift() {
        return etj_shift;
    }

    public void setEtj_shift(eTJ_Shift etj_shift) {
        this.etj_shift = etj_shift;
    }

}