





import java.util.List;
import java.util.ArrayList;

public class pimm_Fifo extends PiMMVisitable {

    private String type;
    private String id;





    private pimm_PiGraph pimm_pigraph;




    private pimm_DataOutputPort pimm_dataoutputport;




    private pimm_DataOutputPort pimm_dataoutputport;




    private pimm_DataInputPort pimm_datainputport;




    private pimm_DataInputPort pimm_datainputport;


    public pimm_Fifo(
        String type,        String id    ) {
        super(
        );
        this.type = type;
        this.id = id;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public pimm_PiGraph getPimm_pigraph() {
        return pimm_pigraph;
    }

    public void setPimm_pigraph(pimm_PiGraph pimm_pigraph) {
        this.pimm_pigraph = pimm_pigraph;
    }
    public pimm_DataOutputPort getPimm_dataoutputport() {
        return pimm_dataoutputport;
    }

    public void setPimm_dataoutputport(pimm_DataOutputPort pimm_dataoutputport) {
        this.pimm_dataoutputport = pimm_dataoutputport;
    }
    public pimm_DataOutputPort getPimm_dataoutputport() {
        return pimm_dataoutputport;
    }

    public void setPimm_dataoutputport(pimm_DataOutputPort pimm_dataoutputport) {
        this.pimm_dataoutputport = pimm_dataoutputport;
    }
    public pimm_DataInputPort getPimm_datainputport() {
        return pimm_datainputport;
    }

    public void setPimm_datainputport(pimm_DataInputPort pimm_datainputport) {
        this.pimm_datainputport = pimm_datainputport;
    }
    public pimm_DataInputPort getPimm_datainputport() {
        return pimm_datainputport;
    }

    public void setPimm_datainputport(pimm_DataInputPort pimm_datainputport) {
        this.pimm_datainputport = pimm_datainputport;
    }

}