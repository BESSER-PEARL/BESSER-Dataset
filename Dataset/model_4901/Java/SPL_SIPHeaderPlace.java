





import java.util.List;
import java.util.ArrayList;

public class SPL_SIPHeaderPlace extends Place {

    private String header;



    public SPL_SIPHeaderPlace(
        String header    ) {
        super(
        );
        this.header = header;
    }


    public String getHeader() {
        return header;
    }

    public void setHeader(String header) {
        this.header = header;
    }


}