





import java.util.List;
import java.util.ArrayList;

public class jpdl31_MetricInfo  {

    private String name;





    private jpdl31_Metric jpdl31_metric;




    private jpdl31_TaskNodeType jpdl31_tasknodetype;




    private jpdl31_TaskType jpdl31_tasktype;


    public jpdl31_MetricInfo(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jpdl31_Metric getJpdl31_metric() {
        return jpdl31_metric;
    }

    public void setJpdl31_metric(jpdl31_Metric jpdl31_metric) {
        this.jpdl31_metric = jpdl31_metric;
    }
    public jpdl31_TaskNodeType getJpdl31_tasknodetype() {
        return jpdl31_tasknodetype;
    }

    public void setJpdl31_tasknodetype(jpdl31_TaskNodeType jpdl31_tasknodetype) {
        this.jpdl31_tasknodetype = jpdl31_tasknodetype;
    }
    public jpdl31_TaskType getJpdl31_tasktype() {
        return jpdl31_tasktype;
    }

    public void setJpdl31_tasktype(jpdl31_TaskType jpdl31_tasktype) {
        this.jpdl31_tasktype = jpdl31_tasktype;
    }

}