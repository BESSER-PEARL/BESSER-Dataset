





import java.util.List;
import java.util.ArrayList;

public class CheckIn_Entity  {

    private String QRCode;
    private String CheckInStatus;
    private String MobileKey;
    private String paymentMode;
    private String PickUpAddress;





    private PostStay_Entity poststay_entity;


    public CheckIn_Entity(
        String QRCode,        String CheckInStatus,        String MobileKey,        String paymentMode,        String PickUpAddress    ) {
        this.QRCode = QRCode;
        this.CheckInStatus = CheckInStatus;
        this.MobileKey = MobileKey;
        this.paymentMode = paymentMode;
        this.PickUpAddress = PickUpAddress;
    }


    public String getQrcode() {
        return QRCode;
    }

    public void setQrcode(String QRCode) {
        this.QRCode = QRCode;
    }
    public String getCheckinstatus() {
        return CheckInStatus;
    }

    public void setCheckinstatus(String CheckInStatus) {
        this.CheckInStatus = CheckInStatus;
    }
    public String getMobilekey() {
        return MobileKey;
    }

    public void setMobilekey(String MobileKey) {
        this.MobileKey = MobileKey;
    }
    public String getPaymentmode() {
        return paymentMode;
    }

    public void setPaymentmode(String paymentMode) {
        this.paymentMode = paymentMode;
    }
    public String getPickupaddress() {
        return PickUpAddress;
    }

    public void setPickupaddress(String PickUpAddress) {
        this.PickUpAddress = PickUpAddress;
    }

    public PostStay_Entity getPoststay_entity() {
        return poststay_entity;
    }

    public void setPoststay_entity(PostStay_Entity poststay_entity) {
        this.poststay_entity = poststay_entity;
    }

}