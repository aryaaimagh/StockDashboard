import plotly.express as px
import pandas as pd


def create_bar_chart(df, x, y, title, text_auto=True):
    fig = px.bar(df, x=x, y=y, title=title, color_discrete_sequence=px.colors.qualitative.Plotly)

    fig.update_layout(
        title={
            'text': title,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'      
        },
        yaxis={
            'tickfont': {'size': 20},
        },
        xaxis_title="",
        yaxis_title="",
        legend_title="",
        barmode="group",
        xaxis={
            'tickmode': 'linear',
            'tick0': 1,
            'tickfont': {'size': 20}
        }
    )
    fig.update_traces(hovertemplate='%{x}<br>%{y:.2f}', hoverlabel=dict(font=dict(size=20)))

    return fig





def create_stack_bar_chart(df, x, y, title, text_auto=True):
    fig = px.bar(df, x=x, y=y, title=title, color_discrete_sequence=px.colors.qualitative.Plotly)

    fig.update_layout(
        title={
            'text': title,
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'      
        },
        yaxis={
            'tickfont': {'size': 20},
        },
        xaxis_title="",
        yaxis_title="",
        legend_title="",
        barmode="stack",
        legend=dict(orientation="h", yanchor="top", xanchor="center", y=1.05, x=0.5),
        xaxis={
            'tickmode': 'linear',
            'tick0': 1,
            'tickfont': {'size': 20}
        }
    )
    fig.update_traces(hovertemplate='%{x}<br>%{y:.2f}')
    return fig