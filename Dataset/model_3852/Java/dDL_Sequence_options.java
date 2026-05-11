





import java.util.List;
import java.util.ArrayList;

public class dDL_Sequence_options  {

    private String nocache;
    private String nocycle;
    private String cycle;
    private String start;
    private String order;
    private String minvalue;
    private String maxvalue;
    private String cache;
    private String nomaxvalue;
    private String nominvalue;
    private String noorder;
    private String increment;





    private dDL_Create_sequence ddl_create_sequence;


    public dDL_Sequence_options(
        String nocache,        String nocycle,        String cycle,        String start,        String order,        String minvalue,        String maxvalue,        String cache,        String nomaxvalue,        String nominvalue,        String noorder,        String increment    ) {
        this.nocache = nocache;
        this.nocycle = nocycle;
        this.cycle = cycle;
        this.start = start;
        this.order = order;
        this.minvalue = minvalue;
        this.maxvalue = maxvalue;
        this.cache = cache;
        this.nomaxvalue = nomaxvalue;
        this.nominvalue = nominvalue;
        this.noorder = noorder;
        this.increment = increment;
    }


    public String getNocache() {
        return nocache;
    }

    public void setNocache(String nocache) {
        this.nocache = nocache;
    }
    public String getNocycle() {
        return nocycle;
    }

    public void setNocycle(String nocycle) {
        this.nocycle = nocycle;
    }
    public String getCycle() {
        return cycle;
    }

    public void setCycle(String cycle) {
        this.cycle = cycle;
    }
    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }
    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }
    public String getMinvalue() {
        return minvalue;
    }

    public void setMinvalue(String minvalue) {
        this.minvalue = minvalue;
    }
    public String getMaxvalue() {
        return maxvalue;
    }

    public void setMaxvalue(String maxvalue) {
        this.maxvalue = maxvalue;
    }
    public String getCache() {
        return cache;
    }

    public void setCache(String cache) {
        this.cache = cache;
    }
    public String getNomaxvalue() {
        return nomaxvalue;
    }

    public void setNomaxvalue(String nomaxvalue) {
        this.nomaxvalue = nomaxvalue;
    }
    public String getNominvalue() {
        return nominvalue;
    }

    public void setNominvalue(String nominvalue) {
        this.nominvalue = nominvalue;
    }
    public String getNoorder() {
        return noorder;
    }

    public void setNoorder(String noorder) {
        this.noorder = noorder;
    }
    public String getIncrement() {
        return increment;
    }

    public void setIncrement(String increment) {
        this.increment = increment;
    }

    public dDL_Create_sequence getDdl_create_sequence() {
        return ddl_create_sequence;
    }

    public void setDdl_create_sequence(dDL_Create_sequence ddl_create_sequence) {
        this.ddl_create_sequence = ddl_create_sequence;
    }

}