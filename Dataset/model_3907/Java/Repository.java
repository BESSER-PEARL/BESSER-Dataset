





import java.util.List;
import java.util.ArrayList;

public class Repository  {






    private pcm_repository_Interface pcm_repository_interface;




    private pcm_repository_DataType pcm_repository_datatype;


    public Repository(
    ) {
    }



    public pcm_repository_Interface getPcm_repository_interface() {
        return pcm_repository_interface;
    }

    public void setPcm_repository_interface(pcm_repository_Interface pcm_repository_interface) {
        this.pcm_repository_interface = pcm_repository_interface;
    }
    public pcm_repository_DataType getPcm_repository_datatype() {
        return pcm_repository_datatype;
    }

    public void setPcm_repository_datatype(pcm_repository_DataType pcm_repository_datatype) {
        this.pcm_repository_datatype = pcm_repository_datatype;
    }

}