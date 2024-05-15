import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu


with st.sidebar:
    select = option_menu('KELOMPOK 2',['NAMA KELOMPOK','Program Json'])

if (select =='NAMA KELOMPOK'):
    st.header('1.Bagus Naufal Abiyyu Putra')
    st.header('2.Cessaro Damova')
    st.header('3.Danar Mas Saputra')
    st.header('4.Devi Oktaviani')
    st.header('5.Dicka Taksa Rabbani')
    st.header('6.Faishal ariq hidayat')

if(select =='Program Json'):

    datas={
            'No': ['1','2','3', '4', '5', '6'],
                    'Gambar Barang':["https://img.freepik.com/free-vector/sticker-template-with-laptop-isolated_1308-58817.jpg?w=900&t=st=1714274121~exp=1714274721~hmac=59a250be2c179d204afea790786017525f7a8ff6b94893f8923b0c701fed5ec8",
                                    "https://img.freepik.com/free-vector/smartphone-front-back_23-2147495562.jpg?w=740&t=st=1714274231~exp=1714274831~hmac=2072d347b1d79761eb4722c07c9ac541cee4ab87a68c74051f0d458edf8b67fd",
                                    "https://i.pinimg.com/564x/f0/f0/36/f0f03693c008e96a8346d38a8095fc72.jpg",
                                    "https://s3.bukalapak.com/img/3880436457/w-1000/GelasKaca200mlGelasUnikGelasMinumanGelasSouvenir_1_scaledjpg.jpg",
                                    "https://i.pinimg.com/originals/9c/73/a9/9c73a95f0646a2fd685f1fccfbdc63c7.jpg",
                                    "https://image1ws.indotrading.com/s3/productimages/co10233/p258240/pulpen-plastic-336-442038.jpg"],
                    'Nama Barang': ['LAPTOP','HP','JAM', 'GELAS', 'BUKU', 'PULPEN'],
                    'Keterangan Barang': ['BARANG 1',
                                        'BARANG 2',
                                        'BARANG 3',
                                        'BARANG 4',
                                        'BARANG 5',
                                        'BARANG 6'
                                        ],
                    'Pemilik': ['Dicka', 'Danar', 'Devi', 'Faishal', 'Bagus', 'Cessaro']
            }
        
    df = pd.DataFrame(datas)
                    
    st.data_editor(
                    datas,
                    column_config={
                        "Gambar Barang": st.column_config.ImageColumn(
                            width = "medium",
                            help = None
                            
                        )
                    },
                    hide_index=True,
                )

