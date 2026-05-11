





import java.util.List;
import java.util.ArrayList;

public class softwaretraces_Trace extends MyNode {

    private int lineNumber;
    private String fileName;
    private String projectName;





    private softwaretraces_Feature softwaretraces_feature;




    private List<softwaretraces_Trace> softwaretraces_traces;




    private softwaretraces_Model softwaretraces_model;


    public softwaretraces_Trace(
        int lineNumber,        String fileName,        String projectName    ) {
        super(
        );
        this.lineNumber = lineNumber;
        this.fileName = fileName;
        this.projectName = projectName;
        this.softwaretraces_traces = new ArrayList<>();
    }

    public softwaretraces_Trace(
        int lineNumber,        String fileName,        String projectName        ArrayList<softwaretraces_Trace> softwaretraces_traces    ) {
        this.lineNumber = lineNumber;
        this.fileName = fileName;
        this.projectName = projectName;
        this.softwaretraces_traces = softwaretraces_traces;
    }

    public int getLinenumber() {
        return lineNumber;
    }

    public void setLinenumber(int lineNumber) {
        this.lineNumber = lineNumber;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }
    public String getProjectname() {
        return projectName;
    }

    public void setProjectname(String projectName) {
        this.projectName = projectName;
    }

    public softwaretraces_Feature getSoftwaretraces_feature() {
        return softwaretraces_feature;
    }

    public void setSoftwaretraces_feature(softwaretraces_Feature softwaretraces_feature) {
        this.softwaretraces_feature = softwaretraces_feature;
    }
    public List<softwaretraces_Trace> getSoftwaretraces_traces() {
        return softwaretraces_traces;
    }

    public void addSoftwaretraces_trace(Softwaretraces_trace softwaretraces_trace) {
        this.softwaretraces_traces.add(softwaretraces_trace);
    }
    public softwaretraces_Model getSoftwaretraces_model() {
        return softwaretraces_model;
    }

    public void setSoftwaretraces_model(softwaretraces_Model softwaretraces_model) {
        this.softwaretraces_model = softwaretraces_model;
    }

}