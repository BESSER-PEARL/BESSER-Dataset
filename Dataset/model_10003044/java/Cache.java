





import java.util.List;
import java.util.ArrayList;

public class Cache  {

    private String chunck;





    private RAM ram;


    public Cache(
        String chunck    ) {
        this.chunck = chunck;
    }


    public String getChunck() {
        return chunck;
    }

    public void setChunck(String chunck) {
        this.chunck = chunck;
    }

    public RAM getRam() {
        return ram;
    }

    public void setRam(RAM ram) {
        this.ram = ram;
    }

}