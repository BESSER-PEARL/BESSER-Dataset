




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class junitresult_Testsuite extends AbstractAggregatedTest {

    private int disabled;
    private String system_out;
    private String hostname;
    private String system_err;
    private LocalDate timestamp;
    private int skipped;
    private String package;
    private int id;
    private float time;





    private List<junitresult_Testcase> junitresult_testcases;


    public junitresult_Testsuite(
        int disabled,        String system_out,        String hostname,        String system_err,        LocalDate timestamp,        int skipped,        String package,        int id,        float time    ) {
        super(
        );
        this.disabled = disabled;
        this.system_out = system_out;
        this.hostname = hostname;
        this.system_err = system_err;
        this.timestamp = timestamp;
        this.skipped = skipped;
        this.package = package;
        this.id = id;
        this.time = time;
        this.junitresult_testcases = new ArrayList<>();
    }

    public junitresult_Testsuite(
        int disabled,        String system_out,        String hostname,        String system_err,        LocalDate timestamp,        int skipped,        String package,        int id,        float time        ArrayList<junitresult_Testcase> junitresult_testcases    ) {
        this.disabled = disabled;
        this.system_out = system_out;
        this.hostname = hostname;
        this.system_err = system_err;
        this.timestamp = timestamp;
        this.skipped = skipped;
        this.package = package;
        this.id = id;
        this.time = time;
        this.junitresult_testcases = junitresult_testcases;
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
    public String getHostname() {
        return hostname;
    }

    public void setHostname(String hostname) {
        this.hostname = hostname;
    }
    public String getSystem_err() {
        return system_err;
    }

    public void setSystem_err(String system_err) {
        this.system_err = system_err;
    }
    public LocalDate getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDate timestamp) {
        this.timestamp = timestamp;
    }
    public int getSkipped() {
        return skipped;
    }

    public void setSkipped(int skipped) {
        this.skipped = skipped;
    }
    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public float getTime() {
        return time;
    }

    public void setTime(float time) {
        this.time = time;
    }

    public List<junitresult_Testcase> getJunitresult_testcases() {
        return junitresult_testcases;
    }

    public void addJunitresult_testcase(Junitresult_testcase junitresult_testcase) {
        this.junitresult_testcases.add(junitresult_testcase);
    }

}