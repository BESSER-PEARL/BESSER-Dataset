





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsView extends RdbmsElement {

    private String originUuid;



    public rdbms_RdbmsView(
        String originUuid    ) {
        super(
        );
        this.originUuid = originUuid;
    }


    public String getOriginuuid() {
        return originUuid;
    }

    public void setOriginuuid(String originUuid) {
        this.originUuid = originUuid;
    }


}