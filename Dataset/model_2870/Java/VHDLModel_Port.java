





import java.util.List;
import java.util.ArrayList;

public class VHDLModel_Port  {

    private String name;
    private boolean high;





    private VHDLModel_Port vhdlmodel_port;




    private VHDLModel_Block vhdlmodel_block;




    private VHDLModel_ComplexBlock vhdlmodel_complexblock;


    public VHDLModel_Port(
        String name,        boolean high    ) {
        this.name = name;
        this.high = high;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getHigh() {
        return high;
    }

    public void setHigh(boolean high) {
        this.high = high;
    }

    public VHDLModel_Port getVhdlmodel_port() {
        return vhdlmodel_port;
    }

    public void setVhdlmodel_port(VHDLModel_Port vhdlmodel_port) {
        this.vhdlmodel_port = vhdlmodel_port;
    }
    public VHDLModel_Block getVhdlmodel_block() {
        return vhdlmodel_block;
    }

    public void setVhdlmodel_block(VHDLModel_Block vhdlmodel_block) {
        this.vhdlmodel_block = vhdlmodel_block;
    }
    public VHDLModel_ComplexBlock getVhdlmodel_complexblock() {
        return vhdlmodel_complexblock;
    }

    public void setVhdlmodel_complexblock(VHDLModel_ComplexBlock vhdlmodel_complexblock) {
        this.vhdlmodel_complexblock = vhdlmodel_complexblock;
    }

}