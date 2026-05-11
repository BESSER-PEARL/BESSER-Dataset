




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class junitresult_Testsuite extends AbstractAggregatedTest {

    private int skipped;
    private String system_err;
    private String package;
    private String hostname;
    private int disabled;
    private String system_out;
    private LocalDate timestamp;
    private float time;
    private int id;





    private List<junitresult_Property> junitresult_propertys;


    public junitresult_Testsuite(
        int skipped,        String system_err,        String package,        String hostname,        int disabled,        String system_out,        LocalDate timestamp,        float time,        int id    ) {
        super(
        );
        this.skipped = skipped;
        this.system_err = system_err;
        this.package = package;
        this.hostname = hostname;
        this.disabled = disabled;
        this.system_out = system_out;
        this.timestamp = timestamp;
        this.time = time;
        this.id = id;
        this.junitresult_propertys = new ArrayList<>();
    }

    public junitresult_Testsuite(
        int skipped,        String system_err,        String package,        String hostname,        int disabled,        String system_out,        LocalDate timestamp,        float time,        int id        ArrayList<junitresult_Property> junitresult_propertys    ) {
        this.skipped = skipped;
        this.system_err = system_err;
        this.package = package;
        this.hostname = hostname;
        this.disabled = disabled;
        this.system_out = system_out;
        this.timestamp = timestamp;
        this.time = time;
        this.id = id;
        this.junitresult_propertys = junitresult_propertys;
    }

    public int getSkipped() {
        return skipped;
    }

    public void setSkipped(int skipped) {
        this.skipped = skipped;
    }
    public String getSystem_err() {
        return system_err;
    }

    public void setSystem_err(String system_err) {
        this.system_err = system_err;
    }
    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }
    public String getHostname() {
        return hostname;
    }

    public void setHostname(String hostname) {
        this.hostname = hostname;
    }
    public int getDisabled() {
        return disabled;
    }

    public void setDisabled(int disabled) {
        this.disabled = disabled;
    }
    public String getSystem_out() {
        return system_out;
    }

    public void setSystem_out(String system_out) {
        this.system_out = system_out;
    }
    public LocalDate getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDate timestamp) {
        this.timestamp = timestamp;
    }
    public float getTime() {
        return time;
    }

    public void setTime(float time) {
        this.time = time;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<junitresult_Property> getJunitresult_propertys() {
        return junitresult_propertys;
    }

    public void addJunitresult_property(Junitresult_property junitresult_property) {
        this.junitresult_propertys.add(junitresult_property);
    }

}