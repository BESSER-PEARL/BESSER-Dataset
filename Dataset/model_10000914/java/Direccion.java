





import java.util.List;
import java.util.ArrayList;

public class Direccion  {

    private String municipio;
    private int idDireccion;
    private int idMunicipio;
    private String estado;
    private String asentamiento;
    private String tipo;
    private int cp;
    private String zona;
    private String ciudad;
    private int idEstado;



    public Direccion(
        String municipio,        int idDireccion,        int idMunicipio,        String estado,        String asentamiento,        String tipo,        int cp,        String zona,        String ciudad,        int idEstado    ) {
        this.municipio = municipio;
        this.idDireccion = idDireccion;
        this.idMunicipio = idMunicipio;
        this.estado = estado;
        this.asentamiento = asentamiento;
        this.tipo = tipo;
        this.cp = cp;
        this.zona = zona;
        this.ciudad = ciudad;
        this.idEstado = idEstado;
    }


    public String getMunicipio() {
        return municipio;
    }

    public void setMunicipio(String municipio) {
        this.municipio = municipio;
    }
    public int getIddireccion() {
        return idDireccion;
    }

    public void setIddireccion(int idDireccion) {
        this.idDireccion = idDireccion;
    }
    public int getIdmunicipio() {
        return idMunicipio;
    }

    public void setIdmunicipio(int idMunicipio) {
        this.idMunicipio = idMunicipio;
    }
    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }
    public String getAsentamiento() {
        return asentamiento;
    }

    public void setAsentamiento(String asentamiento) {
        this.asentamiento = asentamiento;
    }
    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public int getCp() {
        return cp;
    }

    public void setCp(int cp) {
        this.cp = cp;
    }
    public String getZona() {
        return zona;
    }

    public void setZona(String zona) {
        this.zona = zona;
    }
    public String getCiudad() {
        return ciudad;
    }

    public void setCiudad(String ciudad) {
        this.ciudad = ciudad;
    }
    public int getIdestado() {
        return idEstado;
    }

    public void setIdestado(int idEstado) {
        this.idEstado = idEstado;
    }


}