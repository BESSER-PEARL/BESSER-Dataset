





import java.util.List;
import java.util.ArrayList;

public class jbatch_ItemProcessor  {

    private String ref;





    private jbatch_Properties jbatch_properties;




    private jbatch_Chunk jbatch_chunk;


    public jbatch_ItemProcessor(
        String ref    ) {
        this.ref = ref;
    }


    public String getRef() {
        return ref;
    }

    public void setRef(String ref) {
        this.ref = ref;
    }

    public jbatch_Properties getJbatch_properties() {
        return jbatch_properties;
    }

    public void setJbatch_properties(jbatch_Properties jbatch_properties) {
        this.jbatch_properties = jbatch_properties;
    }
    public jbatch_Chunk getJbatch_chunk() {
        return jbatch_chunk;
    }

    public void setJbatch_chunk(jbatch_Chunk jbatch_chunk) {
        this.jbatch_chunk = jbatch_chunk;
    }

}