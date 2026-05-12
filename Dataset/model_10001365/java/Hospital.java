





import java.util.List;
import java.util.ArrayList;

public class Hospital  {

    private String address;
    private int phone;
    private String name;





    private RFID_Reader rfid_reader;




    private List<RFID_Reader> rfid_readers;




    private List<RFID_Reader> rfid_readers;


    public Hospital(
        String address,        int phone,        String name    ) {
        this.address = address;
        this.phone = phone;
        this.name = name;
        this.rfid_readers = new ArrayList<>();
        this.rfid_readers = new ArrayList<>();
    }

    public Hospital(
        String address,        int phone,        String name        ArrayList<RFID_Reader> rfid_readers,        ArrayList<RFID_Reader> rfid_readers    ) {
        this.address = address;
        this.phone = phone;
        this.name = name;
        this.rfid_readers = rfid_readers;
        this.rfid_readers = rfid_readers;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public RFID_Reader getRfid_reader() {
        return rfid_reader;
    }

    public void setRfid_reader(RFID_Reader rfid_reader) {
        this.rfid_reader = rfid_reader;
    }
    public List<RFID_Reader> getRfid_readers() {
        return rfid_readers;
    }

    public void addRfid_reader(Rfid_reader rfid_reader) {
        this.rfid_readers.add(rfid_reader);
    }
    public List<RFID_Reader> getRfid_readers() {
        return rfid_readers;
    }

    public void addRfid_reader(Rfid_reader rfid_reader) {
        this.rfid_readers.add(rfid_reader);
    }

}