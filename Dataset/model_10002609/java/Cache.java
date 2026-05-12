





import java.util.List;
import java.util.ArrayList;

public class Cache  {

    private String chunck;





    private List<Processor> processors;


    public Cache(
        String chunck    ) {
        this.chunck = chunck;
        this.processors = new ArrayList<>();
    }

    public Cache(
        String chunck        ArrayList<Processor> processors    ) {
        this.chunck = chunck;
        this.processors = processors;
    }

    public String getChunck() {
        return chunck;
    }

    public void setChunck(String chunck) {
        this.chunck = chunck;
    }

    public List<Processor> getProcessors() {
        return processors;
    }

    public void addProcessor(Processor processor) {
        this.processors.add(processor);
    }

}