





import java.util.List;
import java.util.ArrayList;

public class analysis_buffers_OptimalBufferData  {






    private BoundedBuffersReport boundedbuffersreport;




    private BottlenecksWithSchedulingReport bottleneckswithschedulingreport;


    public analysis_buffers_OptimalBufferData(
    ) {
    }



    public BoundedBuffersReport getBoundedbuffersreport() {
        return boundedbuffersreport;
    }

    public void setBoundedbuffersreport(BoundedBuffersReport boundedbuffersreport) {
        this.boundedbuffersreport = boundedbuffersreport;
    }
    public BottlenecksWithSchedulingReport getBottleneckswithschedulingreport() {
        return bottleneckswithschedulingreport;
    }

    public void setBottleneckswithschedulingreport(BottlenecksWithSchedulingReport bottleneckswithschedulingreport) {
        this.bottleneckswithschedulingreport = bottleneckswithschedulingreport;
    }

}