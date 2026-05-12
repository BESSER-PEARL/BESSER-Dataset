





import java.util.List;
import java.util.ArrayList;

public class connection_XmlXPathLoopDescriptor  {

    private String LimitBoucle;
    private String AbsoluteXPathQuery;





    private connection_XmlFileConnection connection_xmlfileconnection;




    private connection_SchemaTarget connection_schematarget;




    private List<connection_SchemaTarget> connection_schematargets;




    private connection_XmlFileConnection connection_xmlfileconnection;


    public connection_XmlXPathLoopDescriptor(
        String LimitBoucle,        String AbsoluteXPathQuery    ) {
        this.LimitBoucle = LimitBoucle;
        this.AbsoluteXPathQuery = AbsoluteXPathQuery;
        this.connection_schematargets = new ArrayList<>();
    }

    public connection_XmlXPathLoopDescriptor(
        String LimitBoucle,        String AbsoluteXPathQuery        ArrayList<connection_SchemaTarget> connection_schematargets    ) {
        this.LimitBoucle = LimitBoucle;
        this.AbsoluteXPathQuery = AbsoluteXPathQuery;
        this.connection_schematargets = connection_schematargets;
    }

    public String getLimitboucle() {
        return LimitBoucle;
    }

    public void setLimitboucle(String LimitBoucle) {
        this.LimitBoucle = LimitBoucle;
    }
    public String getAbsolutexpathquery() {
        return AbsoluteXPathQuery;
    }

    public void setAbsolutexpathquery(String AbsoluteXPathQuery) {
        this.AbsoluteXPathQuery = AbsoluteXPathQuery;
    }

    public connection_XmlFileConnection getConnection_xmlfileconnection() {
        return connection_xmlfileconnection;
    }

    public void setConnection_xmlfileconnection(connection_XmlFileConnection connection_xmlfileconnection) {
        this.connection_xmlfileconnection = connection_xmlfileconnection;
    }
    public connection_SchemaTarget getConnection_schematarget() {
        return connection_schematarget;
    }

    public void setConnection_schematarget(connection_SchemaTarget connection_schematarget) {
        this.connection_schematarget = connection_schematarget;
    }
    public List<connection_SchemaTarget> getConnection_schematargets() {
        return connection_schematargets;
    }

    public void addConnection_schematarget(Connection_schematarget connection_schematarget) {
        this.connection_schematargets.add(connection_schematarget);
    }
    public connection_XmlFileConnection getConnection_xmlfileconnection() {
        return connection_xmlfileconnection;
    }

    public void setConnection_xmlfileconnection(connection_XmlFileConnection connection_xmlfileconnection) {
        this.connection_xmlfileconnection = connection_xmlfileconnection;
    }

}