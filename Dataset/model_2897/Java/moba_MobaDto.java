





import java.util.List;
import java.util.ArrayList;

public class moba_MobaDto extends MobaData {

    private String name;





    private moba_MobaTransportSerializationType moba_mobatransportserializationtype;




    private moba_MobaDto moba_mobadto;




    private moba_MobaEntity moba_mobaentity;


    public moba_MobaDto(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public moba_MobaTransportSerializationType getMoba_mobatransportserializationtype() {
        return moba_mobatransportserializationtype;
    }

    public void setMoba_mobatransportserializationtype(moba_MobaTransportSerializationType moba_mobatransportserializationtype) {
        this.moba_mobatransportserializationtype = moba_mobatransportserializationtype;
    }
    public moba_MobaDto getMoba_mobadto() {
        return moba_mobadto;
    }

    public void setMoba_mobadto(moba_MobaDto moba_mobadto) {
        this.moba_mobadto = moba_mobadto;
    }
    public moba_MobaEntity getMoba_mobaentity() {
        return moba_mobaentity;
    }

    public void setMoba_mobaentity(moba_MobaEntity moba_mobaentity) {
        this.moba_mobaentity = moba_mobaentity;
    }

}