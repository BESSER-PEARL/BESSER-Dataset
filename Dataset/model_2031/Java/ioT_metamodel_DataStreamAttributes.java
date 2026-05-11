





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_DataStreamAttributes  {

    private String MeanBitRate;
    private String DeviceID;
    private String Description;
    private String DataFormat;
    private String DataEncoding;
    private String MaxBitrate;
    private String Timestamp;





    private ioT_metamodel_DataStreams iot_metamodel_datastreams;


    public ioT_metamodel_DataStreamAttributes(
        String MeanBitRate,        String DeviceID,        String Description,        String DataFormat,        String DataEncoding,        String MaxBitrate,        String Timestamp    ) {
        this.MeanBitRate = MeanBitRate;
        this.DeviceID = DeviceID;
        this.Description = Description;
        this.DataFormat = DataFormat;
        this.DataEncoding = DataEncoding;
        this.MaxBitrate = MaxBitrate;
        this.Timestamp = Timestamp;
    }


    public String getMeanbitrate() {
        return MeanBitRate;
    }

    public void setMeanbitrate(String MeanBitRate) {
        this.MeanBitRate = MeanBitRate;
    }
    public String getDeviceid() {
        return DeviceID;
    }

    public void setDeviceid(String DeviceID) {
        this.DeviceID = DeviceID;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public String getDataformat() {
        return DataFormat;
    }

    public void setDataformat(String DataFormat) {
        this.DataFormat = DataFormat;
    }
    public String getDataencoding() {
        return DataEncoding;
    }

    public void setDataencoding(String DataEncoding) {
        this.DataEncoding = DataEncoding;
    }
    public String getMaxbitrate() {
        return MaxBitrate;
    }

    public void setMaxbitrate(String MaxBitrate) {
        this.MaxBitrate = MaxBitrate;
    }
    public String getTimestamp() {
        return Timestamp;
    }

    public void setTimestamp(String Timestamp) {
        this.Timestamp = Timestamp;
    }

    public ioT_metamodel_DataStreams getIot_metamodel_datastreams() {
        return iot_metamodel_datastreams;
    }

    public void setIot_metamodel_datastreams(ioT_metamodel_DataStreams iot_metamodel_datastreams) {
        this.iot_metamodel_datastreams = iot_metamodel_datastreams;
    }

}