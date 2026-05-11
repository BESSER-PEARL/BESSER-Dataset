





import java.util.List;
import java.util.ArrayList;

public class dataflow_Port extends Attributable {

    private String name;





    private dataflow_Actor dataflow_actor;




    private dataflow_Buffer dataflow_buffer;




    private dataflow_Buffer dataflow_buffer;




    private dataflow_Actor dataflow_actor;




    private List<dataflow_Buffer> dataflow_buffers;




    private dataflow_Buffer dataflow_buffer;




    private dataflow_Actor dataflow_actor;


    public dataflow_Port(
        String name    ) {
        super(
        );
        this.name = name;
        this.dataflow_buffers = new ArrayList<>();
    }

    public dataflow_Port(
        String name        ArrayList<dataflow_Buffer> dataflow_buffers    ) {
        this.name = name;
        this.dataflow_buffers = dataflow_buffers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dataflow_Actor getDataflow_actor() {
        return dataflow_actor;
    }

    public void setDataflow_actor(dataflow_Actor dataflow_actor) {
        this.dataflow_actor = dataflow_actor;
    }
    public dataflow_Buffer getDataflow_buffer() {
        return dataflow_buffer;
    }

    public void setDataflow_buffer(dataflow_Buffer dataflow_buffer) {
        this.dataflow_buffer = dataflow_buffer;
    }
    public dataflow_Buffer getDataflow_buffer() {
        return dataflow_buffer;
    }

    public void setDataflow_buffer(dataflow_Buffer dataflow_buffer) {
        this.dataflow_buffer = dataflow_buffer;
    }
    public dataflow_Actor getDataflow_actor() {
        return dataflow_actor;
    }

    public void setDataflow_actor(dataflow_Actor dataflow_actor) {
        this.dataflow_actor = dataflow_actor;
    }
    public List<dataflow_Buffer> getDataflow_buffers() {
        return dataflow_buffers;
    }

    public void addDataflow_buffer(Dataflow_buffer dataflow_buffer) {
        this.dataflow_buffers.add(dataflow_buffer);
    }
    public dataflow_Buffer getDataflow_buffer() {
        return dataflow_buffer;
    }

    public void setDataflow_buffer(dataflow_Buffer dataflow_buffer) {
        this.dataflow_buffer = dataflow_buffer;
    }
    public dataflow_Actor getDataflow_actor() {
        return dataflow_actor;
    }

    public void setDataflow_actor(dataflow_Actor dataflow_actor) {
        this.dataflow_actor = dataflow_actor;
    }

}