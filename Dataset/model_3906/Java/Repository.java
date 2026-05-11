





import java.util.List;
import java.util.ArrayList;

public class Repository  {






    private pcm_repository_DataType pcm_repository_datatype;




    private pcm_repository_ProvidesComponentType pcm_repository_providescomponenttype;




    private pcm_repository_Interface pcm_repository_interface;


    public Repository(
    ) {
    }



    public pcm_repository_DataType getPcm_repository_datatype() {
        return pcm_repository_datatype;
    }

    public void setPcm_repository_datatype(pcm_repository_DataType pcm_repository_datatype) {
        this.pcm_repository_datatype = pcm_repository_datatype;
    }
    public pcm_repository_ProvidesComponentType getPcm_repository_providescomponenttype() {
        return pcm_repository_providescomponenttype;
    }

    public void setPcm_repository_providescomponenttype(pcm_repository_ProvidesComponentType pcm_repository_providescomponenttype) {
        this.pcm_repository_providescomponenttype = pcm_repository_providescomponenttype;
    }
    public pcm_repository_Interface getPcm_repository_interface() {
        return pcm_repository_interface;
    }

    public void setPcm_repository_interface(pcm_repository_Interface pcm_repository_interface) {
        this.pcm_repository_interface = pcm_repository_interface;
    }

}